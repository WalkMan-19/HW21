from classes import *

shop = Shop(items={
    "печенье": 7,
    "собака": 2,
    "ёлка": 1,
    'ноут': 1,
})
store = Store(items={
    "печенье": 28,
    "собака": 19,
    "ёлка": 23,
})

storages = {
    'магазин': shop,
    'склад': store,
}


def create_store():
    while True:

        print('_' * 25)
        for storage in storages:
            print(f'Сейчас в {storage} имеется:\n{storages[storage].get_items()}\n')

        user_input = input(
            'Введите запрос в формате "Доставить 3 печенье из склад в магазин"\n'
            'Введите "стоп" или "stop", если хотите закончить:\n'
        )

        if user_input.lower() in ['stop', 'стоп']:
            break
        
        try:
            request = Request(request=user_input)

        except BadRequest as br:
            print(br.message)
            continue

        delivery = Delivery(
            request=request,
            storages=storages,
        )

        try:
            delivery.move()
        except BaseError as e:
            print(e.message)


if __name__ == '__main__':
    create_store()
