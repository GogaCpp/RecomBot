import telebot
from handlers import start, quiz, help
import os
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv("TOKEN"))

start.register_handlers(bot)
help.register_handlers(bot)
quiz.register_handlers(bot)

if __name__ == '__main__':
    bot.polling(none_stop=True)
