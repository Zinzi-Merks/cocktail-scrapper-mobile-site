import os
import pandas as pd

def find_recipes(name: str):
  # Load CSV containing all recipes
  # https://towardsdatascience.com/how-to-read-csv-file-using-pandas-ab1f5e7e7b58
  df = pd.read_csv('cocktails_all.csv', sep=';')

  # Filter recipes by ingredient
  # https://stackoverflow.com/a/27975230
  df = df[df['ingredients'].str.contains(name, case=False, na=False)]
  return df.values.tolist()