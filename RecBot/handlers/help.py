from telebot import TeleBot


def register_handlers(bot: TeleBot):
    @bot.message_handler(commands=['help'])
    def help_message(message):
        chat_id = message.chat.id
        text= """
        Команды:
        /start - запуск бота
        /help - справочная информация о командей
        /opros - выбор места отдыха

Работу сделали студенты 114 группы:
        Авакян Александр
        Грушецкий Генадий
        Елизаров Андрей
        """
        text = text.replace("\t", "")
        bot.send_message(chat_id, text)
