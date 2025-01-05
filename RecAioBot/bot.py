import telebot
from config import TOKEN
from handlers import start, quiz


bot = telebot.TeleBot(TOKEN)

start.register_handlers(bot)
quiz.register_handlers(bot)


if __name__ == '__main__':
    bot.polling(none_stop=True)
