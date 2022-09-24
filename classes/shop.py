from classes.exceptions import ShopIsFull
from classes.storage import Storage


class Shop(Storage):
    def __init__(self, items: dict, capacity=20) -> None:
        super().__init__(items, capacity)

    def add(self, k, v) -> None:
        if self.get_unique_items_count() <= 5:  # добавление товара если видов товара <= 5
            super().add(k=k, v=v)
        else:
            raise ShopIsFull

    def remove(self, k, v) -> None:
        super().remove(k=k, v=v)

    def get_free_space(self) -> int:
        return super().get_free_space()

    def get_items(self) -> dict:
        return super().get_items()

    def get_unique_items_count(self) -> int:
        return super().get_unique_items_count()
