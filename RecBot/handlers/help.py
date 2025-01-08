from telebot import TeleBot, types


def register_handlers(bot: TeleBot):
    @bot.message_handler(commands=['help'])
    def help_message(message):
        chat_id = message.chat.id
        text = """
        Команды:
        /start - запуск бота
        /help - справочная информация о команде
        /places - выбор места отдыха

Работу сделали студенты 114 группы:
        Елизаров Андрей
        Грушецкий Генадий
        Авакян Александр
        """
        text = text.replace("\t", "")
        media = []
        with open("RecBot/images/we.jpeg", 'rb') as photo:
            media.append(types.InputMediaPhoto(photo, caption=text))
            bot.send_media_group(chat_id, media)

