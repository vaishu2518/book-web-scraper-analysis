
# Book Web Scraper and Data Analysis

## Project Overview
This project uses Python to scrape book information from the
Books to Scrape website, clean the collected data, perform
exploratory data analysis, and generate visualizations.

## Objectives
- Collect book titles, prices, ratings, and availability.
- Clean and prepare the dataset.
- Calculate descriptive statistics.
- Analyze ratings and stock availability.
- Compare average prices across rating groups.
- Visualize findings using charts.

## Technologies Used
- Python
- Requests
- BeautifulSoup
- Pandas
- Matplotlib

## Project Structure
- `webscrapping.py` - Scrapes book information.
- `clean_data.py` - Cleans and transforms the dataset.
- `analysis.py` - Performs analysis and generates charts.
- `books_data.csv` - Raw scraped data.
- `books_data_cleaned.csv` - Cleaned dataset.
- `price_distribution.png` - Book price distribution chart.
- `ratings_distribution.png` - Ratings distribution chart.
- `stock_availability.png` - Stock availability chart.
- `requirements.txt` - Required Python packages.

## How to Run the Project

### 1. Install dependencies
```bash
python -m pip install -r requirements.txt
```

### 2. Scrape the data
```bash
python webscrapping.py
```

### 3. Clean the data
```bash
python clean_data.py
```

### 4. Analyze the data
```bash
python analysis.py
```

## Analysis Performed
- Average, minimum, and maximum book prices.
- Most common book rating.
- Stock availability percentage.
- Highest-priced and lowest-priced books.
- Average price by rating.
- Correlation between price and rating.

## Visualizations
The project generates:
1. Price distribution histogram.
2. Ratings distribution bar chart.
3. Stock availability bar chart.

## Data Source
https://books.toscrape.com/

This website is intended for practicing web scraping.

## Limitations
- The analysis covers only the pages scraped by the script.
- The dataset represents a snapshot of the website.
- Price-rating correlation does not establish causation.
- Results should not be generalized to all books or retailers.

## Future Improvements
- Build an interactive dashboard.
- Add more data-quality checks.
- Expand the analysis and reporting.
- Compare findings across larger datasets.
