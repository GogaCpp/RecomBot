import requests
from telebot import TeleBot
from keyboards.get_location_K import get_location_keyboard
from telebot.types import Message, ReplyKeyboardRemove
import os
from dotenv import load_dotenv


def register_handlers(bot: TeleBot):
    @bot.message_handler(commands=['start_location'])
    def ask_location(message):
        bot.send_message(
            message.chat.id,
            "Пожалуйста, отправьте свою геолокацию:",
            reply_markup=get_location_keyboard()
        )
        bot.register_next_step_handler(message, location_handler, bot)

    def location_handler(message: Message, bot: TeleBot):
        if message.location:
            latitude = message.location.latitude
            longitude = message.location.longitude
            null_markup = ReplyKeyboardRemove()
            bot.send_message(
                message.chat.id,
                f"Ваши координаты: Широта: {latitude}, Долгота: {longitude}",
                reply_markup=null_markup
            )
        if message.text:
            make_request(message)

    def make_request(message):

        load_dotenv()
        api_key = os.getenv("API_KEY")
        addres = message.text

        responce = requests.get(
            f"https://catalog.api.2gis.com/3.0/items/geocode?q={addres}&fields=items.point&key={api_key}"
            )
        responce = responce.json()
        print(responce)
        lat = responce["result"]["items"][0]["point"]["lat"]
        lon = responce["result"]["items"][0]["point"]["lon"]
        null_markup = ReplyKeyboardRemove()
        bot.send_message(
                message.chat.id,
                f"Ваши координаты: Широта: {lat}, Долгота: {lon}",
                reply_markup=null_markup
            )
