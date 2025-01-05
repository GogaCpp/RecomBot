import telebot
# from config import TOKEN
from handlers import start, quiz, location
import os
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv("TOKEN"))

start.register_handlers(bot)
quiz.register_handlers(bot)
location.register_handlers(bot)

if __name__ == '__main__':
    bot.polling(none_stop=True)
