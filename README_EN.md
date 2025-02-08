# IMDb Movie Parser

## English 🇬🇧  
This project is a web scraper that extracts movie data from IMDb's Top 250 list. It collects movie names, release years, ratings, number of votes, and URLs, and saves them to a CSV file.

### Features:
- Uses `BeautifulSoup` and `Selenium` to scrape IMDb.
- Saves the extracted data in `final_list.csv`.
- Automates scrolling to load all data.

### Requirements:
- Python 3.x
- `beautifulsoup4`, `selenium`, `lxml`

### Usage:
1. Install dependencies:  
   ```bash
   pip install beautifulsoup4 selenium lxml
