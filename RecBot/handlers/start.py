from telebot import TeleBot


def register_handlers(bot: TeleBot):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        chat_id = message.chat.id
        text = "Привет! Я ваш бот по подбору места для отдыха\nВся справочная информация тут 👉 /help"
        bot.send_message(chat_id, text)

