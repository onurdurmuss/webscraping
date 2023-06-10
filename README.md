# NBA Player Data Scraping
This repository contains scripts to scrape NBA player data including player name, salary, year of the salary, player page link, and birth date from [Hoopshype](https://hoopshype.com/). We used three different libraries for scraping: Beautiful Soup, Scrapy, and Selenium.

## Prerequisites
You need to have Python 3.x installed on your machine. If you don't have Python installed you can find it [here](https://www.python.org/downloads/).

Additionally, you need to have the following Python packages installed. You can install these packages using pip:
- BeautifulSoup
- Scrapy
- Selenium
- pandas
- requests

You can install the necessary packages with the following command:
```python 
pip install beautifulsoup4 pandas requests scrapy selenium
```

For Selenium, you'll also need to have the correct WebDriver installed for your browser of choice:

- Chrome: [ChromeDriver](https://sites.google.com/chromium.org/driver/)
- Firefox: [GeckoDriver](https://github.com/mozilla/geckodriver/releases)

**Note:** Make sure to add the WebDriver executable to your system PATH.

## How to Run the Scripts

### Beautiful Soup
To run the Beautiful Soup scraper, run the following command in your terminal:
```python 
python beautiful_soup_scraper.py
```
This script will output a CSV file named `player_salaries_bs.csv` in the same directory.

### Scrapy
Before running the Scrapy scraper, ensure you are in the directory where the `players.py` file (or whatever your scrapy spider file is named) is located. Then, you can run the spider using the Scrapy command:
```python 
scrapy crawl players -o player_salaries.csv
```

The `-o` flag tells Scrapy to output the data to a file. The script outputs a csv file named `player_salaries.csv`.

### Selenium
Before running the Selenium script, make sure you have the correct WebDriver installed for your browser and added to your system PATH.

In the provided Selenium script, the WebDriver for Chrome (chromedriver) is used. If you want to use another browser, make sure to change the code accordingly.

To run the Selenium scraper, run the following command in your terminal:
```python 
python selenium_scraper.py
```

This script will output a CSV file named `player_salaries.csv` in the same directory.

---

**Note:** Web scraping should be done responsibly. Make sure to respect the terms of service or robots.txt files of the websites you are scraping. These scripts may also require updates if the layout of the website changes.



