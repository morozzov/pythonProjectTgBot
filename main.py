import datetime
import telebot
from telebot import types
from bs4 import BeautifulSoup
import requests as req

bot = telebot.TeleBot("5130068690:AAFOtDL61iI6UnUuNYLpF65FBJ7RHfbM5fM")

def parseQuote():
    resp = req.get("http://bashorg.org/random")
    soup = BeautifulSoup(resp.text, 'lxml')
    soup = soup.find("div", class_="quote").getText(separator="\n")
    return soup

def parseJoke():
    resp = req.get("https://baneks.ru/random")
    soup = BeautifulSoup(resp.text, 'lxml')
    soup = soup.find("p").getText(separator="\n")
    return soup

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Quote")
    markup.add(item1)
    item2 = types.KeyboardButton("Joke")
    markup.add(item2)
    bot.send_message(m.chat.id, "Click: \nQuote to show random quote\nJoke to show random joke", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == "Quote":
        answer = parseQuote()
    elif message.text.strip() == "Joke":
        answer = parseJoke()
    else:
        answer = "ERROR"
    print(datetime.datetime.now(), end=": ")
    print(message.text.strip())
    bot.send_message(message.chat.id, answer)

print("start")
bot.polling(none_stop=True, interval=0)