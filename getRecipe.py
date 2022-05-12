from asyncio.windows_events import NULL
import requests
from variables import apiKey
url = f"https://api.spoonacular.com/recipes/random?apiKey={apiKey}"

def getRandomRecipe():
    response = requests.get(url)
    response = response.json()["recipes"]
    for data in response:
        title = data["title"]
        readyInMinutes = data["readyInMinutes"]
        servings = data["servings"]
        recipeUrl = data["spoonacularSourceUrl"]
        vegetarian = data["vegetarian"]
        vegan = data["vegan"]
        credits = data["creditsText"]

        message = f"""
{title} 😋 {"(Vegan Recipe)" if vegan else ""}{"(Vegetarian Recipe)" if vegetarian else ""}
Ready in {readyInMinutes} minutes 🕒
{servings} servings 👨‍🍳\n
Read more about this recipe in {recipeUrl}

Ingredients:
        """
        for ingredient in data["extendedIngredients"]:
            message = message+f"""
🔸 {ingredient['original']}
            """
        
        message = message+f"\nCredits to {credits}"
        
        return message