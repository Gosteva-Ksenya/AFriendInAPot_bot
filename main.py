import functions
import telebot
import settings

bot = telebot.TeleBot(settings.TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome1(message):
    functions.send_welcome(message)


@bot.message_handler(commands=['go'])
def go_to1(message):
    functions.go_to(message)


@bot.message_handler(content_types=['text'])
def mess1(message):
    functions.mess(message)


bot.infinity_polling()
