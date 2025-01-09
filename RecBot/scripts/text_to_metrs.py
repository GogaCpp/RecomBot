import re
from ru_word2number import w2n


def convert_to_meters(distance_str):
    distance_str = distance_str.strip().lower()

    km_to_meters = 1000
    meters_to_meters = 1

    distance_value = None

    for unit in ['км', 'километр', 'метров', 'м', 'метр']:
        distance_str_clean = distance_str.replace(unit, '')

    try:
        distance_value = w2n.word_to_num(distance_str_clean.strip())
    except ValueError:
        match = re.search(r'(\d+(\.\d+)?)', distance_str)
        if match:
            distance_value = float(match.group(0))

    if distance_value is not None:
        original_distance_str = distance_str.strip()
        if 'км' in original_distance_str or 'километр' in original_distance_str:
            return int(distance_value * km_to_meters)
        elif 'м' in original_distance_str or 'метр' in original_distance_str:
            return int(distance_value * meters_to_meters)
        else:
            return distance_value
    return None


if __name__ == "__main__":
    print(convert_to_meters("1 км"))
    print(convert_to_meters("1км"))
    print(convert_to_meters("10000 метров"))
    print(convert_to_meters("5 километров"))
    print(convert_to_meters("1000 МЕТРОВ"))
    print(convert_to_meters("1.5 КИЛОМЕТРА"))
    print(convert_to_meters("один километр"))
    print(convert_to_meters("двести метров"))
    print(convert_to_meters("два километра"))
    print(convert_to_meters("А если 1.5 км"))
    print(convert_to_meters("А ЕСЛИ 2.28КИЛОМЕТРОВЫХ ПОБЕГУШЕК СЫНОК!!!"))
    print(convert_to_meters("1000"))
