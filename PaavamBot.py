import os
from dotenv import load_dotenv
import telebot

load_dotenv()
key = os.getenv('API_KEY')
bot = telebot.TeleBot(key)

@bot.message_handler(commands=["greet"])
def greet(msg):
    bot.send_message(msg.chat.id, "hellooooo")

bot.polling()
