import logging
import requests as r
import os
from dotenv import load_dotenv
from pprint import pprint


def find_nearby_places(api_key, lon, lat, place_type, radius=1000):

    url = f"""
    https://catalog.api.2gis.com/3.0/items?
    q={place_type}&
    point={lon},{lat}&
    sort_point={lon},{lat}&
    sort=rating&
    radius={radius}&
    fields=items.full_address_name,items.reviews,items.point,items.address,items.schedule&
    key={api_key}
    """

    url = url.replace("\n", "").replace("\t", "").replace(" ", "")
    logging.info("request {url}")
    response = r.get(url)

    if response.status_code == 200:
        results = response.json()
        # pprint(results)  # ! удалить(ручной дебаг)
        if results["meta"]["code"] != 200:  # Хорошо что гении на 2gis отдают 200 даже на ошибки(наверное grafQl)
            logging.error(f"Request error {results['meta']['error']}")
            return None
        return results
    else:  # ? на всякий, я в душе не чаю что у них там на уме
        logging.error(f"Ошибка: {response.status_code}, {response.text}")
        return None


if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv('API_KEY')
    place_type = "кафе"
    lon = "38.019281"
    lat = "55.631671"  # учитывать порядок так как 2gis черти (lon,lat)
    radius = "1000"

    res = find_nearby_places(api_key=api_key, lon=lon, lat=lat, place_type=place_type, radius=radius)
    pprint(res)
