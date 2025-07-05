# Dynamic Autoscraper

A powerful, intelligent web scraping tool that combines Playwright for JavaScript rendering and Autoscraper for pattern learning. This tool can extract data from dynamic, JavaScript-heavy websites by learning from examples and supports multi-page crawling with pagination.

## ✨ Features

- **🔄 Dynamic Content Loading**: Uses Playwright to render JavaScript-heavy websites
- **🧠 Intelligent Data Extraction**: Learns extraction patterns using Autoscraper
- **📄 Multi-page Crawling**: Supports pagination to crawl through multiple pages
- **📊 Structured Output**: Saves results in clean CSV format
- **🐳 Docker Support**: Containerized deployment for easy setup
- **⚡ Multiple Extraction Methods**: Combines Autoscraper with BeautifulSoup for robust data extraction
- **🛡️ Error Handling**: Graceful error handling and recovery
- **📝 Comprehensive Logging**: Detailed progress tracking and debugging

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Hardik-Joshi123/dynamic-autoscraper.git
   cd dynamic-autoscraper
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   playwright install --with-deps
   ```

3. **Configure your scrape**
   Edit `config.json` with your target website and examples:
   ```json
   {
     "start_urls": ["https://example.com/articles"],
     "examples": ["Example headline text"],
     "pagination_selector": ".next-page"
   }
   ```

4. **Run the scraper**
   ```bash
   python scraper.py
   ```

## 📋 Configuration

### config.json Structure
```json
{
  "start_urls": [
    "https://example.com/page1",
    "https://example.com/page2"
  ],
  "examples": [
    "Example text to extract",
    "Another example pattern"
  ],
  "pagination_selector": ".next-page"
}
```

### Configuration Options
- **`start_urls`**: Array of URLs to start scraping from
- **`examples`**: Array of example text patterns to learn from
- **`pagination_selector`**: CSS selector for the "next page" link (optional)

## 🐳 Docker Usage

### Build the Docker image
```bash
docker build -t dynamic-autoscraper .
```

### Run with Docker
```bash
docker run --rm -v $(pwd)/results:/app/results dynamic-autoscraper
```

## 📊 Output

The scraper saves results to `results/output.csv` with the following structure:
```csv
results
"Extracted text 1"
"Extracted text 2"
"Extracted text 3"
...
```

## 🔧 How It Works

1. **Training Phase**: Autoscraper learns extraction patterns from your examples
2. **Page Loading**: Playwright loads each page and renders JavaScript content
3. **Data Extraction**: Multiple methods extract data from the rendered HTML
4. **Pagination**: Follows "next page" links to crawl multiple pages
5. **Deduplication**: Removes duplicate results
6. **Output**: Saves clean data to CSV format

## 🛠️ Development

### Project Structure
```
dynamic-autoscraper/
├── scraper.py          # Main scraping script
├── config.json         # Configuration file
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── README.md          # This file
├── .gitignore         # Git ignore rules
├── LICENSE            # MIT License
└── results/           # Output directory (created automatically)
    └── output.csv     # Scraped results
```

### Adding New Features
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Contributing Guidelines
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


---

