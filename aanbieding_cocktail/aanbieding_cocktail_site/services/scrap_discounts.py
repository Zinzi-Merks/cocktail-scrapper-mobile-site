from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
from bs4 import BeautifulSoup

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# The website that is going to be scraped
site = "https://www.gall.nl/acties/"
parameters = "/?banners=0&start="

# The Gall&Gall website has 12 items per page
def scrap_discounts(filter, page, max_length = 12):
  driver = webdriver.Chrome(chrome_options=options)
  discounts = []

  # Start scraping
  # Format url: https://www.gall.nl/acties/<NAME_OF_DRINK_CATEGORY>/?banners=0&start=<PAGE_NUMBER>
  driver.get(site + filter + parameters + str(page*max_length))
  soup = BeautifulSoup(driver.page_source, features="html.parser")

  # scrape names, prices, images and urls from page
  names_page = [name.text for name in soup.select('.ptile-v2_link strong[itemprop="name"]')]
  prices_page = [price['aria-label'] for price in soup.select('.price-v2')]
  image_url_page = [image['src'] for image in soup.select('.ptile-v2_link img')]
  url_page = [url['href'] for url in soup.select('.ptile-v2_link')]

  for index in range(len(names_page)):
    discounts.append({
      'name': names_page[index],
      'price': prices_page[index],
      'image_url': image_url_page[index],
      'url': 'https://www.gall.nl/' + url_page[index]
    })

  return discounts
