import os
from dotenv import load_dotenv
import telebot

load_dotenv()
key = os.getenv('API_KEY')
bot = telebot.TeleBot(key)

@bot.message_handler(commands=["aara"])
def greet(msg):
    bot.send_message(msg.chat.id, "njan oru paavam")

bot.polling()
