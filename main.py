import telebot
import requests
import random

from telebot.types import ReplyKeyboardMarkup, KeyboardButton

API_KEY = '5e309bbc01d94ba1a38b35daa17f38a9'
TOKEN = '7193970620:AAHbZv71P7vJJpPcJ8IZ4L21vT9Fat_HZOk'
URL_RECEPT_API = 'https://api.spoonacular.com/recipes/random?apiKey=5e309bbc01d94ba1a38b35daa17f38a9'

bot = telebot.TeleBot(TOKEN)

keyboard = ReplyKeyboardMarkup(resize_keyboard = True)
keyboard.add(KeyboardButton('Узнать название блюда'))
keyboard.add(KeyboardButton('О проекте'))

@bot.message_handler(regexp='Узнать название блюда')
def send_recipe(message):
    r = requests.get(url = URL_RECEPT_API)
    text = (r.json()["recipes"][0]["title"])
    text2 = (r.json()["recipes"][0]["summary"])
    bot.send_message(message.chat.id, text, reply_markup=keyboard)
    bot.send_message(message.chat.id, text2, reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = "Привет, я бот, который может выдавать разные названия блюд, давай поработаем"
    bot.send_message(message.chat.id, text, reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    text = ("Ну я бот и вот")
    bot.send_message(message.chat.id, text, reply_markup=keyboard)


@bot.message_handler(regexp='О проекте')
def send_about(message):
    text = 'Проект написал Ефимов Василий. НазваниеБлюдБот. Приятного аппетита'
    bot.send_message(message.chat.id, text, reply_markup=keyboard)
bot.infinity_polling()

