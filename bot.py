import telebot
from bs4 import BeautifulSoup
import requests


TOKEN = '***********************'
bot = telebot.TeleBot(TOKEN)


def internet_search(msg):
    # еще не придумал
    url = f'https:/www.google.com/search?q={msg}'


@bot.message_handler(commands=['start', 'help'])
def start_help_message(message):
    bot.reply_to(message, 'Привет, я поисковой бот, отправь мне запрос и я найду по нему информацию в интернете')


@bot.message_handler(func=lambda message: True)
def get_and_reply(message):
    msg = message.text
    reply = internet_search(msg)
    bot.reply_to(message, reply)


bot.infinity_polling()