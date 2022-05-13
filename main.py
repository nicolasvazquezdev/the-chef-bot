import telebot
from getRecipe import getRecipe
from variables import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['getRecipe'])
def send_randomRecipe(message):
    chatId = message.from_user.id
    message = message.text.split()[1::] # Get the words next to the command. Those will be the tags to search the recipe
    tags = " ".join(message)
    if(getRecipe(tags) != None):
        bot.send_message(chatId, getRecipe(tags))
    else:
        bot.send_message(chatId, "I couldn't find a recipe with those characteristics. Try something else 🔁")

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
        bot.send_message(chatId, "Do you want a recipe? Send the command /getRecipe 🤖")

bot.infinity_polling()