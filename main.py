from time import sleep
import telebot
from getRecipe import getRecipe
from variables import token
from datetime import datetime

bot = telebot.TeleBot(token)
now = datetime.now()
if(now.minute <= 9):
    minutes = f"0{now.minute}"
else:
    minutes = now.minute
if(now.hour <= 9):
    hour = f"0{now.hour}"
else:
    hour = now.hour

schedule = f"{hour}:{minutes}"

# /help
@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, """
Hey!
If you want a recipe, send the command /getRecipe
You can also search a recipe with a parameter, example:
/getRecipe ice cream
/getRecipe vegan
/getRecipe dinner
    """)

# /getRecipe
@bot.message_handler(commands=['getRecipe'])
def send_recipe(message):
    chatId = message.from_user.id
    message = message.text.split()[1::] # Get the words next to the command. Those will be the tags to search the recipe
    tags = " ".join(message)
    if(getRecipe(tags) != None):
        bot.send_message(chatId, getRecipe(tags))
    else:
        bot.send_message(chatId, "I couldn't find a recipe with those characteristics. Try something else 🔁")

# /setRecipe
recipesScheduled = []
chat_id = ""
@bot.message_handler(commands=['setRecipe'])
def setRecipe(message):
    messageUser = message.text.split()[1::] # Get the words next to the command. Those will be the tags to search the recipe
    commandMessage = " ".join(messageUser).split(" ")
    commandTag = commandMessage[1]
    commandSchedule = commandMessage[0]
    newRecipe = {"schedule": commandSchedule, "tag": commandTag}
    recipesScheduled.append(newRecipe)
    
# Send the recipes that were scheduled
def sendScheduledRecipes():
    while True == True:
        print(recipesScheduled)
        print("----")
        sleep(1)
sendScheduledRecipes()


@bot.message_handler()
def echo_all(message):
    chatId = message.from_user.id
    userMsg = message.text.lower()

    if("hello" in userMsg or "hi" in userMsg):
        bot.send_message(chatId, "Hey! Let's go to cook something 👩‍🍳")
    elif("bye" in userMsg):
        bot.send_message(chatId, "See you 👋")
    elif("thanks" in userMsg):
        bot.send_message(chatId, "You're welcome 🙏")
    else:
        bot.send_message(chatId, "I don't understand. If you need help, send the comand /help 🤖")

bot.infinity_polling()