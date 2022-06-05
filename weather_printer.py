from get_weather import Weather


def print_weather(weather: Weather, city) -> str:
    return (f'В городе {city} температура {weather.temperature} градусов. '
            f'На улице {weather.weather_type}. '
            f'{weather.wind_dir} направление ветра со скоростью {weather.wind_speed} м/с'
            )
