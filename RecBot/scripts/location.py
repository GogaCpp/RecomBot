import requests
import os
from dotenv import load_dotenv


def make_location_request(message):
    load_dotenv()
    api_key = os.getenv("API_KEY")
    addres = message.text

    responce = requests.get(
        f"https://catalog.api.2gis.com/3.0/items/geocode?q={addres}&fields=items.point&key={api_key}"
        )
    if responce.status_code == 200:
        responce = responce.json()
        lat = responce["result"]["items"][0]["point"]["lat"]
        lon = responce["result"]["items"][0]["point"]["lon"]
        return {"lat": lat, "lon": lon}
    else:
        return None
