from classes.storage import Storage


class Store(Storage):
    def __init__(self, items: dict, capacity=100):
        super().__init__(items, capacity)

    def add(self, k, v) -> None:
        super().add(k=k, v=v)

    def remove(self, k, v) -> None:
        super().remove(k=k, v=v)

    def get_free_space(self) -> int:
        return super().get_free_space()

    def get_items(self) -> dict:
        return super().get_items()

    def get_unique_items_count(self) -> int:
        return super().get_unique_items_count()
