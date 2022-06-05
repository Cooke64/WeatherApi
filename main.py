from excteptions import CantGetPlace
from get_data import get_response, get_coordinates
from get_weather import represent_weather
from weather_printer import print_weather


def main() -> str:
    city = input('Введите город')
    try:
        coord = get_coordinates(city)
    except:
        raise CantGetPlace('Нет города с такими координатами')
    response = get_response(*coord)
    weather = represent_weather(response)
    return print_weather(weather, city)


if __name__ == '__main__':
    print(main())
