class CantGetPlace(Exception):
    """Такого гора не существует."""


class ResponseError(Exception):
    """Ошибка запроса к API."""


class CantGetEndpoint(Exception):
    """Смотри документацию API. Вход заблокирован"""


