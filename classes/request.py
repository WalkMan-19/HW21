from classes.exceptions import BadRequest


class Request:
    def __init__(self, request: str):
        split_req = request.lower().split(" ")

        self.amount = int(split_req[1])
        self.product = str(split_req[2])
        self.departure = str(split_req[4])
        self.destination = str(split_req[6])

        if len(split_req) != 7 or self.departure == self.destination:   # доставить из магазин в магазин
            raise BadRequest
