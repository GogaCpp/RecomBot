from telebot import TeleBot


def register_handlers(bot: TeleBot):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Привет! Я ваш бот по подбору места для отдыха") 

# TODO help в подсказку старт
# TODO новый опрос в конууе опроса