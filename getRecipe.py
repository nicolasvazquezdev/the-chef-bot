from asyncio.windows_events import NULL
import requests
from variables import apiKey

def getRecipe(tags=""):
    url = f"https://api.spoonacular.com/recipes/random?tags={tags}&apiKey={apiKey}"
    response = requests.get(url)
    response = response.json()["recipes"]
    for data in response:
        title = data["title"]
        readyInMinutes = data["readyInMinutes"]
        servings = data["servings"]
        recipeUrl = data["spoonacularSourceUrl"]
        vegetarian = data["vegetarian"]
        vegan = data["vegan"]
        image = data["image"]

        message = f"""
{title} 😋{" - Vegan" if vegan else ""}{" - Vegetarian" if vegetarian else ""}
Ready in {readyInMinutes} minutes 🕒
{servings} servings 👨‍🍳

Ingredients:
        """
        for ingredient in data["extendedIngredients"]:
            message = message+f"""
🔸 {ingredient['original']}
            """
        
        message = message+f"""
{image}
\nRead more about this recipe in {recipeUrl}\n
        """
        
        return message