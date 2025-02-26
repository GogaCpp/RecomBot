from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def get_location_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    location_button_map = KeyboardButton("Отправить свою геолокацию", request_location=True)
    keyboard.add(location_button_map)
    return keyboard
