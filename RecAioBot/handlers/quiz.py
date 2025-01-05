from telebot import TeleBot
from telebot.types import Message

questions = [
    "Как вас зовут?",
    "Сколько вам лет?",
    "Какой у вас любимый цвет?"
]

user_responses = {}


def survey_handler(message: Message, bot: TeleBot, question_index=0):
    chat_id = message.chat.id

    if chat_id not in user_responses:
        user_responses[chat_id] = []

    if question_index < len(questions):
        if question_index == 0:
            bot.send_message(chat_id, questions[question_index])
        else:
            user_responses[chat_id].append(message.text)
            bot.send_message(chat_id, questions[question_index])

        bot.register_next_step_handler(message, survey_handler, bot, question_index + 1)
    else:
        # Завершение опроса
        user_responses[chat_id].append(message.text)
        bot.send_message(chat_id, "Спасибо за участие в опросе!")
        print(user_responses[chat_id])
        del user_responses[chat_id]


def register_handlers(bot: TeleBot):
    @bot.message_handler(commands=['opros'])
    def handle_opros(message: Message):
        survey_handler(message, bot)
