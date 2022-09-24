from classes.exceptions import ErrorAddresses
from classes.request import Request
from classes.storage import Storage


class Delivery:
    def __init__(self, request: Request, storages: dict[str, Storage]):
        self._request = request

        if self._request.departure in storages and self._request.destination in storages:
            self._from = storages[self._request.departure]
            self._to = storages[self._request.destination]
        else:
            raise ErrorAddresses

    def move(self):
        self._from.remove(k=self._request.product, v=self._request.amount)  # Забрал
        print('Курьер забрал {} в количестве {} из {}'.format(
            self._request.product, self._request.amount, self._request.departure
        ))

        self._to.add(k=self._request.product, v=self._request.amount)  # Доставил
        print('Курьер доставил {} в количестве {} в {}'.format(
            self._request.product, self._request.amount, self._request.destination
        ))
