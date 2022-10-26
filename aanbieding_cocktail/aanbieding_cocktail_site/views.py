from django.shortcuts import render
from aanbieding_cocktail_site.services.scrap_discounts import scrap_discounts
from aanbieding_cocktail_site.services.find_recipes import find_recipes

# Create your views here.

def index(request):
  return render(request, 'site/site.html')

def data(request):
  # Get parameters from url: https://stackoverflow.com/a/150518
  filter = request.GET.get('filter', '')
  page = int(request.GET.get('page', '0'))

  data = scrap_discounts(filter, page)
  return render(request, 'site/discounts_data.html', {'data': data, 'filter': filter})

def list_recipes(request, name: str):
  data = find_recipes(name)

  # Translate string to list of string for ingredients and steps
  for recipe in data:
    recipe[3] = recipe[3].replace("'", '').replace('[', '').replace(']', '').split(',')
    recipe[4] = recipe[4].replace("'", '').replace('[', '').replace(']', '').split(',')

  return render(request, 'recipes/recipes.html', {'data': data, 'ingredient': name})
