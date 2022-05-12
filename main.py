import telebot
from getRecipe import getRandomRecipe

token = "5361423911:AAGMzF25f_YnRBV6egY3MyFg7mqxo-MDJVU"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['randomRecipe'])
def send_randomRecipe(message):
    chatId = message.from_user.id
    bot.send_message(chatId, getRandomRecipe())

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    chatId = message.from_user.id
    if("hola" in message.text.lower()):
        bot.send_message(chatId, "¡Hola! ¿Vamos a cocinar algo? 👩‍🍳")
    elif("chau" in message.text.lower() or "adios" in message.text.lower()):
        bot.send_message(chatId, "Nos vemos 👋")
    else:
        bot.send_message(chatId, "Soy un bot. No te entiendo 🤖")

bot.infinity_polling()