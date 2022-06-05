import json
from enum import Enum
from json import JSONDecodeError
from typing import NamedTuple

from excteptions import ResponseError

Celsius = int


class WeatherType(Enum):
    clear = 'Ясно'
    partly_cloudy = 'Малооблачно'
    cloudy = 'Облачно'
    overcast = 'Пасмурно'
    rain = 'Дождь'
    moderate_rain = 'Умеренно'
    heavy_rain = 'Сильный дождь'
    continuous_heavy_rain = 'Длительный сильный дождь'
    showers = 'Ливень'
    wet_snow = 'Дождь со снегом'
    light_snow = 'Небольшой снег'
    snow = 'Снег'
    snow_showers = 'Снегопад'
    hail = 'Град'
    thunderstorm = 'Гроза'
    thunderstorm_with_rain = 'Дождь с грозой'
    thunderstorm_with_hail = 'Гроза с градом'


class WindType(Enum):
    nw = 'Северо - западное'
    n = 'Северное'
    ne = 'Северо - восточное'
    e = 'Восточное'
    se = 'Юго - восточное'
    s = 'Южное'
    sw = 'Юго - западное'
    w = 'Западное'
    c = 'Штиль'


class Weather(NamedTuple):
    temperature: Celsius
    weather_type: WeatherType
    wind_dir: WindType
    wind_speed: int


def represent_weather(response) -> Weather:
    """Отображение погоды."""
    try:
        weather_dict = json.loads(response.text)
    except JSONDecodeError:
        raise ResponseError
    return Weather(
        temperature=parse_temp(weather_dict),
        weather_type=parse_type(weather_dict),
        wind_dir=parse_wind_dir(weather_dict),
        wind_speed=parse_wind_speed(weather_dict)
    )


def parse_temp(weather: dict) -> Celsius:
    """Парсит текущую температуру."""
    return weather['fact']['temp']


def parse_type(weather: dict) -> WeatherType or str:
    """Парсит тип погоды."""
    weather_type = str(weather['fact']['condition']).replace('-', '_')
    for i in WeatherType:
        if i.name == weather_type:
            return i.value
        else:
            return weather_type


def parse_wind_dir(weather: dict) -> WindType or str:
    """Парсит тип ветра."""
    wind_type = str(weather['fact']['wind_dir']).replace('-', '_')
    for i in WindType:
        if i.name == wind_type:
            return i.value
        else:
            return wind_type


def parse_wind_speed(weather: dict) -> int:
    """Парсит скорость ветра."""
    return weather['fact']['wind_speed']
