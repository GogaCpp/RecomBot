import re


def convert_to_meters(distance_str):

    km_to_meters = 1000
    meters_to_meters = 1

    distance_str = distance_str.strip().lower()

    match = re.search(r'(\d+(\.\d+)?)', distance_str)
    if match:
        distance_value = float(match.group(0))

    if 'км' in distance_str or 'километр' in distance_str:
        return int(distance_value * km_to_meters)
    elif 'м' in distance_str or 'метр' in distance_str:
        return int(distance_value * meters_to_meters)
    return None
