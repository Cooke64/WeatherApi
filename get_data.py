import os
from typing import NamedTuple

import requests
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
from requests import Response

from excteptions import CantGetPlace, ResponseError, CantGetEndpoint


load_dotenv()
WEATHER_TOKEN = os.getenv('WEATHER_TOKEN')
LANG = 'ru_RU'
HEADERS = {'X-Yandex-API-Key': WEATHER_TOKEN}


class Coordinates(NamedTuple):
    latitude: int
    longitude: int


def get_coordinates(city) -> Coordinates:
    """Получаем координаты указанного места."""
    geolocator = Nominatim(user_agent="test")
    try:
        location = geolocator.geocode(city)
    except:
        raise CantGetPlace
    return Coordinates(location.latitude, location.longitude)


def get_response(lat, lon) -> Response:
    """Функция получает ответ от сервиса."""
    url = f'https://api.weather.yandex.ru/v1/forecast?lat={lat}&lon={lon}&lang=[{LANG}]'
    req = requests.get(url, headers=HEADERS)
    if req.status_code == 403:
        raise CantGetEndpoint
    elif req.status_code == 200:
        return req
    raise ResponseError
