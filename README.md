# Dynamic Autoscraper

A general-purpose, dynamic, and automated web scraper that can extract data from paginated, JavaScript-driven websites by learning from user-provided examples, and save the results in a structured CSV format.

## Features
- Loads dynamic JavaScript content with Playwright
- Extracts data by learning patterns with Autoscraper
- Crawls multiple pages using pagination
- Saves results to CSV

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   playwright install --with-deps
   ```
   Or use Docker:
   ```bash
   docker build -t dynamic-autoscraper .
   docker run --rm -v $(pwd)/results:/app/results dynamic-autoscraper
   ```

2. Configure your scrape in `config.json`:
   ```json
   {
     "start_urls": ["https://example.com/articles"],
     "examples": ["Example headline text"],
     "pagination_selector": "a.next-page"
   }
   ```

## Usage

Run the scraper:
```bash
python scraper.py
```

Results will be saved to `results/output.csv`.

## Notes
- Make sure your `examples` in `config.json` match the data you want to extract.
- The `pagination_selector` should be a CSS selector for the "next page" link/button.
