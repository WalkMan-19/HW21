class BaseError(Exception):
    message = 'unexpected error'


class NotFreeSpace(BaseError):
    message = 'Недостаточно мест на складе'


class NotProducts(BaseError):
    message = 'Недостаточно товаров на складе'


class ItemNotExist(BaseError):
    message = 'Такого товара нету'


class ShopIsFull(BaseError):
    message = 'В магазине нету места'


class BadRequest(BaseError):
    message = 'Неправильный запрос'


class ErrorAddresses(BaseError):
    message = 'Неправильно указан адрес'
