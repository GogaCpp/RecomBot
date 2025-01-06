from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardRemove
import os
from dotenv import load_dotenv

from keyboards.get_location_K import get_location_keyboard
from scripts.location import make_location_request
from scripts.scriptlocation import find_nearby_places

load_dotenv()
questions = [
    {"place_type": "Где бы вы хотели погулять?"},
    {"location": "Поделитесь своими геоданными или напишите свой адресс"},
    {"radius": "Как далеко готовы пройтись?"}
]
days_of_week = ["Fri", "Mon", "Sat", "Sun", "Thu", "Tue", "Wed"]
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
        bot.send_message(chat_id, "Ожидайте свою подборочку)")

        text = get_nearby_places(chat_id)
        if text is None:
            text = "По вышим данным ничего не найденно, давайте еще раз\n/opros"
        print(user_responses)
        bot.send_message(chat_id, text)
        del user_responses[chat_id]


def get_nearby_places(chat_id):
    json_resp = find_nearby_places(
        api_key=os.getenv("API_KEY"),
        lat=user_responses[chat_id]["location"]["lat"],
        lon=user_responses[chat_id]["location"]["lon"],
        place_type=user_responses[chat_id]["place_type"],
        radius=user_responses[chat_id]["radius"]
        )
    if json_resp is None:
        return None
    return json_to_text(json_resp)


def json_to_text(json_format):
    text_format = ""
    for num, place in enumerate(json_format["result"]["items"], start=1):
        if num > 5:
            break
        text_format += f'{num}) {place["name"]}\n'
        if place["reviews"].get("general_rating"):
            text_format += f'\t\tРейтинг этого места {place["reviews"]["general_rating"]} 🌟\n'
        if place.get("address") and place["address"].get("components"):
            if place["address"]["components"][0].get("number") and place["address"]["components"][0].get("street"):
                street = place["address"]["components"][0]["street"]
                numbr = place["address"]["components"][0]["number"]
                text_format += f'\t\tАдресс {street} {numbr}🗺\n'
        if place.get("schedule"):
            text_format += "\t\tРасписание🗓: \n"
            for day in place["schedule"]:
                if day in days_of_week:
                    from_time = place["schedule"][day]["working_hours"][0]["from"]
                    to_time = place["schedule"][day]["working_hours"][0]["to"]
                    text_format += f'\t\t\t\t{day} c {from_time} до {to_time}\n'
    return text_format


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
            if resp is None:
                user_responses[chat_id][key]["lat"] = None
                user_responses[chat_id][key]["lon"] = None
            else:
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
