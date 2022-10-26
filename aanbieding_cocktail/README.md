# Cocktail aanbiedingen

## Why this website?

<img src="photo.jpg" alt="drawing" height="200"/>

I wanted to make this website, because my friends and I want to try new drinks but cannot decide what to drink. So I made this website to help us decide what to drink. Because you are trying new drinks, you do not want to spend too much money on a single bottle, that is why I scraped the discounts first from Gall&Gall.

## How do people use it?

When people open the website, they see 5 categories:

- Rum (opens this one by default)
- Vodka
- Whiskey
- Gin
- Likeur

When they click on a category, they see a list of drinks with the discount. Each drink has two buttons: "View discount" and "View recipes". When they click on "View discount", they go to the discount on the Gall&Gall website. When they click on "View recipes", they see a list of recipes based on that category. Each recipe has a name, instruction list, ingredients list and necessities.

## What would a next version include?

- Better recipe filtering. Currently, if a user uses the "View recipe" button within the "Likeuren" category the website might not find recipes for that drink. I have currently 366 recipes, which should be enough, but the name of the drink is used in that category. Sometimes an alias of the drink is used in the recipe or discount, like: "Malibu Coconut", but the recipes only has "Malibu".
- Better loading styling. I tried to make the loading HTML look nice, but was not able to align them above each other in the center of the screen.
- Better styling of the recipes page. Currently, you have a large scrolling page with everything visible. In the next version, you might see a accordion to hide the ingredients and necessities https://getbootstrap.com/docs/5.2/components/accordion/
- More discount sites. Currently, I only scrape the discounts from Gall&Gall, but I would like to add more discount sites.
- Use SerpAPI. If I would use SerpAPI for finding multiple discounts for the same product, just like if you would search that item on Google. https://serpapi.com
