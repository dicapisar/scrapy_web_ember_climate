# Ember Climate Data Scraper

![Ember Climate](https://public.flourish.studio/uploads/1148293/2a0ed913-2c0f-41b9-bf3e-723e420d6b8d.png)

This Python project allows you to scrape carbon pricing data from the Ember Climate website and organize it into Excel spreadsheets for both Euro (EUR) and British Pound (GBP) currencies. By utilizing web scraping techniques and data manipulation libraries, this project extracts and structures data for further analysis and visualization.

## Overview

The project is centered around two main functions:

- `get_ember_climate_info()`: This function scrapes the Ember Climate website using BeautifulSoup, extracting the necessary data from a Flourish visualization.

- `save_ember_climate_info()`: After processing the scraped data, this function categorizes it based on currency and stores it in two separate Excel spreadsheets using pandas.

## Installation and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/dicapisar/scrapy_web_ember_climate.git
   ```

2. Navigate to the project directory:
   ```bash
   cd scrapy_web_ember_climate
   ```

3. Install the required dependencies using the provided `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the main script to initiate data scraping and saving:
   ```bash
   python ember_climate_scraper.py
   ```

5. The extracted data will be neatly organized in the 'datasets.xlsx' Excel file, with separate sheets for 'Dataset_EUR' and 'Dataset_GBP'.

## Example Visualization

Enhance your data analysis with compelling visualizations. Here's a sample representation:

![Sample Visualization](https://example.com/sample-visualization.png)

## Acknowledgments

This project was brought to you by [@dicapisar](https://github.com/dicapisar). For inquiries or contributions, please feel free to reach out.

## Disclaimer

This project is designed for educational purposes. Please use it responsibly and respect the terms of use and scraping guidelines set by the website.

---