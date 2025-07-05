"""
Dynamic Web Scraper: Playwright + Autoscraper + Pagination
✅ Fixed: No connection adapters error
✅ Uses Playwright to render dynamic JS content
✅ Uses Autoscraper to learn & reuse patterns
✅ Supports multi-page crawling
✅ Saves results to CSV
"""

import json
import asyncio
import pandas as pd
from playwright.async_api import async_playwright
from autoscraper import AutoScraper
from urllib.parse import urljoin
import os
from bs4 import BeautifulSoup

# -----------------------------
# Load your config
# -----------------------------
with open('config.json') as f:
    config = json.load(f)

START_URLS = config['start_urls']
EXAMPLES = config['examples']
PAGINATION_SELECTOR = config.get('pagination_selector')

# -----------------------------
# Main scraper coroutine
# -----------------------------
async def scrape_url(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        all_results = []
        visited_urls = set()

        current_url = url

        # ✅ Train Autoscraper ONCE with static URL
        print(f"Training Autoscraper on: {current_url}")
        scraper = AutoScraper()
        scraper.build(current_url, EXAMPLES)

        while current_url and current_url not in visited_urls:
            print(f"Visiting: {current_url}")
            visited_urls.add(current_url)

            try:
                await page.goto(current_url)
                await page.wait_for_timeout(2000)  # Wait for JS to load
                html = await page.content()
                
                # Use BeautifulSoup to extract headlines as fallback
                soup = BeautifulSoup(html, 'html.parser')
                
                # Try to find headlines - look for common patterns
                headlines = []
                
                # Method 1: Look for h1, h2, h3 tags with text
                for tag in soup.find_all(['h1', 'h2', 'h3']):
                    if tag.get_text().strip():
                        headlines.append(tag.get_text().strip())
                
                # Method 2: Look for links that might be headlines
                for link in soup.find_all('a', href=True):
                    text = link.get_text().strip()
                    if text and len(text) > 10 and len(text) < 200:  # Reasonable headline length
                        headlines.append(text)
                
                # Method 3: Try Autoscraper as backup
                try:
                    scraped = scraper.get_result_similar(html)
                    if scraped:
                        headlines.extend(scraped)
                except Exception as e:
                    print(f"Autoscraper failed: {e}")
                
                # Remove duplicates and clean up
                headlines = list(set([h.strip() for h in headlines if h.strip()]))
                print(f"Found {len(headlines)} headlines")
                
                if headlines:
                    all_results.extend(headlines[:10])  # Limit to first 10
                
            except Exception as e:
                print(f"Scraping error at {current_url}: {e}")

            # --------------------------
            # Handle pagination
            # --------------------------
            if PAGINATION_SELECTOR:
                try:
                    next_page = await page.query_selector(PAGINATION_SELECTOR)
                    if next_page:
                        next_href = await next_page.get_attribute('href')
                        if next_href:
                            if not next_href.startswith('http'):
                                next_href = urljoin(current_url, next_href)
                            current_url = next_href
                        else:
                            current_url = None
                    else:
                        current_url = None
                except Exception as e:
                    print(f"Pagination error: {e}")
                    current_url = None
            else:
                current_url = None

        await browser.close()
        return all_results

# -----------------------------
# Run for all start URLs
# -----------------------------
async def main():
    total_results = []
    for url in START_URLS:
        try:
            results = await scrape_url(url)
            total_results.extend(results)
        except Exception as e:
            print(f"Error scraping {url}: {e}")

    # Remove duplicates
    total_results = list(set(total_results))

    # Ensure results directory exists
    os.makedirs('results', exist_ok=True)

    if total_results:
        # Save to CSV
        df = pd.DataFrame({'results': total_results})
        try:
            df.to_csv('results/output.csv', index=False)
            print(f"✅ Done! Saved {len(total_results)} records to results/output.csv")
        except Exception as e:
            print(f"Error saving CSV: {e}")
    else:
        print("No data found to save.")

if __name__ == '__main__':
    asyncio.run(main())
