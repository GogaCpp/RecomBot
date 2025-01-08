import logging
import os
import argparse
from dotenv import load_dotenv
import telebot

from handlers import start, quiz, help

load_dotenv()
bot = telebot.TeleBot(os.getenv("TOKEN"))

start.register_handlers(bot)
help.register_handlers(bot)
quiz.register_handlers(bot)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l", "--loglevel",
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default='INFO', help="Logging level (defoult: INFO)"
    )
    args = parser.parse_args()

    numeric_level = getattr(logging, args.loglevel.upper(), None)  # ! upper ну просто на всякий

    logging.basicConfig(
        level=numeric_level, filename="py_log.log",
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    bot.polling(none_stop=True)
