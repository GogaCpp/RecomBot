from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardRemove

from keyboards.get_location_K import get_location_keyboard
from scripts.location import make_location_request

questions = [
    {"place_type": "Где бы вы хотели погулять?"},
    {"location": "Поделитесь своими геоданными или напишите свой адресс"},
    {"radius": "Как далеко готовы пройтись?"}
]
user_responses = {}  # хешировать id чтобы не присесть от 3 до 8 (пока нет бд не надо, но вообще надо)

null_markup = ReplyKeyboardRemove()


def survey_handler(message: Message, bot: TeleBot, question_index=0):
    chat_id = message.chat.id
    question_markup = null_markup

    if chat_id not in user_responses:
        user_responses[chat_id] = {
            "place_type": None,
            "location": None,
            "radius": None
        }

    if question_index < len(questions):
        if question_index != 0:  # сохранение
            save_message(message, question_index)

        if list(questions[question_index].keys())[0] == "location":
            question_markup = get_location_keyboard()
        bot.send_message(chat_id, list(questions[question_index].values())[0], reply_markup=question_markup)
        bot.register_next_step_handler(message, survey_handler, bot, question_index + 1)
    else:
        save_message(message, question_index)
        bot.send_message(chat_id, "Спасибо за участие в опросе!")
        print(user_responses)
        bot.edit_message_text("негры")
        del user_responses[chat_id]


def save_message(message, question_index):
    chat_id = message.chat.id

    key = list(questions[question_index-1].keys())[0]
    if key == "location":
        user_responses[chat_id][key] = {}
        if message.location:
            latitude = message.location.latitude
            longitude = message.location.longitude

            user_responses[chat_id][key]["lat"] = latitude
            user_responses[chat_id][key]["lon"] = longitude
        else:
            resp = make_location_request(message)
            user_responses[chat_id][key]["lat"] = resp["lat"]
            user_responses[chat_id][key]["lon"] = resp["lon"]

    else:
        user_responses[chat_id][
            list(questions[question_index-1].keys())[0]  # нечитаемая фигня для получения параметра вопроса
            ] = message.text

def register_handlers(bot: TeleBot):
    @bot.message_handler(commands=['opros'])
    def handle_opros(message: Message):
        survey_handler(message, bot)
