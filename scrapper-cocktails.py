from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas
import time
import json

site = 'https://cocktailrecepten.com'

def scrap_site(start, end):
  driver = webdriver.Chrome()
  driver.get(site + '/recepten')
  soup = BeautifulSoup(driver.page_source, features="html.parser")

  # Find all recipes
  urls = []
  for i in range(len(soup.select('.pagination li'))):
    # Because the page loads a 'Vorige' when it is on the second page, we need to skip index 1
    if i == 1:
      continue

    urls.extend([a['href'] for a in soup.select('main .recipe__tile a')])
    driver.find_element(By.CSS_SELECTOR, '.pagination li:nth-child(' + str(i + 1) + ')').click()

    # Wait 1 sec for page to load
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, features="html.parser")

  print(len(urls))

  # Load all the websitepages 
  recipes = []
  for link in range(start, end):
    driver.get(site + urls[link])
    soup = BeautifulSoup(driver.page_source, features="html.parser")

    # Get all ingredients, steps & tools from site
    metadata_site = json.loads(soup.select_one('head script[type="application/ld+json"]').text.replace('\n', ''))

    steps = [step.text for step in soup.select('.instructions-list li p')]
    tools = [tool.text for tool in soup.select('.recipe__tool .title')]

    recipes.append({
      'title': soup.select_one('section .recipe__description h1').text,
      'desc': soup.select_one('section .recipe__description p').text,
      'url': site + urls[link],
      'ingredients': metadata_site['recipeIngredient'],
      'steps': steps,
      'tools': tools
    })
    # Because the ingredientlist takes longer to load it needs 2 extra seconds to load the list
    time.sleep(2)

  return recipes

# The scrapper is not able to scrap all the 480 recipes in one run so it's split in two
data = scrap_site(0, 240)
print(data)

last_240 = scrap_site(241,480)
print (last_240)

# Combain the data from the first and second Scrap_site
data.extend(last_240)

# Make A CSV from the scrapt data
df = pandas.DataFrame(data)
df.to_csv('cocktails_all.csv', index=False, encoding='utf-8')
