
from pprint import pprint
import requests as r
from script_config import api_key

def find_nearby_places(api_key, location, place_type, radius=1000):

    url = f"""
    https://catalog.api.2gis.com/3.0/items?
    q={place_type}&
    point={location}&
    sort_point={location}&
    sort=distance&
    radius={radius}&
    fields=items.full_address_name,items.reviews,items.point&
    key={api_key}
    """

    url = url.replace("\n", "").replace("\t", "").replace(" ", "")
    print(url)
    response = r.get(url)

    if response.status_code == 200:
        results = response.json()
        return results
    else:
        print(f"Ошибка: {response.status_code}, {response.text}")
        return None


if __name__ == "__main__":
    place_type = "кафе"
    location = "38.019281,55.631671"  # учитывать порядок так как 2gis долбоебы
    radius = "1000"

    res = find_nearby_places(api_key=api_key, location=location, place_type=place_type, radius=radius)
    pprint(res)