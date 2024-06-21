import telebot
from bs4 import BeautifulSoup
import requests


TOKEN = '********************************;*'
bot = telebot.TeleBot(TOKEN)


def internet_search(msg):
    url = f'https://www.google.com/search?q={msg}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)
    html_code = BeautifulSoup(response.text, 'html.parser')
    link = html_code.find('div', class_='g').find('a', href=True)
    if link:
        return link['href']
    else:
        return 'По вашему запрорсу ничего не найдено'


@bot.message_handler(commands=['start', 'help'])
def start_help_message(message):
    bot.reply_to(message, 'Привет, я поисковой бот, отправь мне запрос и я найду по нему информацию в интернете')


@bot.message_handler(func=lambda message: True)
def get_and_reply(message):
    msg = message.text
    reply = internet_search(msg)
    bot.reply_to(message, reply)


bot.infinity_polling()
