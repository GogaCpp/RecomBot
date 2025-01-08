from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def get_choice_location_keyboard(location_count: int = 5):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(1, location_count+1):
        keyboard.add(KeyboardButton(f"{i}"))
    return keyboard
