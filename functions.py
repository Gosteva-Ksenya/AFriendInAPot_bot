import telebot
import settings
from telebot import types
import flowers

bot = telebot.TeleBot(settings.TOKEN)


def send_welcome(message):
    bot.reply_to(message.chat.id, "Привет, новый друг! Введи '/go' для начала")


def go_to(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Цветущий')
    btn2 = types.KeyboardButton('Не цветущий')
    markup.add(btn1, btn2)
    bot.reply_to(message.chat.id, "Выбери вариант ответа!", reply_markup=markup)


def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == 'цветущий':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Однолетний')
        btn2 = types.KeyboardButton('Многолетний')
        markup.add(btn1, btn2)
        final_text = 'Сколько будет жить ваш цветок?'

    elif get_message_bot == 'не цветущий':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Высокий')
        btn2 = types.KeyboardButton('Низкий')
        markup.add(btn1, btn2)
        final_text = 'Какой высоты будет ваше растение?'

    elif get_message_bot == 'однолетний':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
        final_text = flowers.Petunia
        photo = open("петуния.jpg", "rb")
        bot.send_photo(message.chat.id, photo)

    elif get_message_bot == 'многолетний':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
        final_text = flowers.Gwozdika
        photo = open("гвоздика.jpg", "rb")
        bot.send_photo(message.chat.id, photo)

    elif get_message_bot == 'высокий':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
        final_text = flowers.Ficus
        photo = open("фикус.jpg", "rb")
        bot.send_photo(message.chat.id, photo)

    elif get_message_bot == 'низкий':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
        final_text = flowers.Kaktus
        photo = open("кактус.jpg", "rb")
        bot.send_photo(message.chat.id, photo)

    bot.reply_to(message, final_text, reply_markup=markup)

