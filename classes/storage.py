from abc import ABC, abstractmethod
from classes.exceptions import NotFreeSpace, NotProducts, ItemNotExist


class Storage(ABC):
    def __init__(self, items: dict, capacity: int):
        self._items = items         # property
        self._capacity = capacity   # property

    @abstractmethod
    def add(self, k: str, v: int) -> None:
        """
        Добавляем количество товара в словарь
        Или новый товар
        """
        if self.get_free_space() >= v:

            if k.lower() in self._items.keys():
                self._items[k] += v

            else:
                self._items[k] = v
        else:
            raise NotFreeSpace

    @abstractmethod
    def remove(self, k: str, v: int):
        """
        Убираем количество товара из словаря
        """
        if k.lower() in self._items.keys():

            if v <= self._items[k]:
                self._items[k] -= v

                if self._items[k] == 0:
                    self._items.pop(k)

            else:
                raise NotProducts
        else:
            raise ItemNotExist

    @abstractmethod
    def get_free_space(self) -> int:
        """
        Подсчёт свободного места
        """
        items_count = 0
        for value in self._items.values():
            items_count += value
        return self._capacity - items_count

    @abstractmethod
    def get_items(self) -> dict:
        """
        Возвращает товары на складе
        """
        return self._items

    @abstractmethod
    def get_unique_items_count(self) -> int:
        """
        Возвращает уникальные названия товаров
        """
        return len(set(self._items.keys()))
