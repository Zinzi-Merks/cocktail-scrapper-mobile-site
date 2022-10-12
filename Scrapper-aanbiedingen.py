from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas
import time

# The website that is going to be scrapt 
site = "https://www.gall.nl/acties/bitters_likeuren_rum_whisky_wodka/?banners=0&start="

def scrap_site():
  driver = webdriver.Chrome()

  discounts = []
  i = 0
  # loop trough all pages of the discount website
  while True:
    driver.get(site + str(i*12))
    soup = BeautifulSoup(driver.page_source, features="html.parser")

    # scrape names and prices from page
    names_page = [name.text for name in soup.select('.ptile-v2_link strong[itemprop="name"]')]
    prices_page = [price['aria-label'] for price in soup.select('.price-v2')]

    # break out of the loop if there are no discounts left
    if len(names_page) == 0:
      break

    i += 1
    for index in range(len(names_page)):
      discounts.append({
        'name': names_page[index],
        'price': prices_page[index]
      })

  print(discounts)
  return discounts

data = scrap_site()

df = pandas.DataFrame(data)
df.to_csv('cocktails_aanbiedingen.csv', index=False, encoding='utf-8')

