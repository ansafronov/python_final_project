from random import randint


def log(string=None):
    """Декоратор для методов процесса приготовления и доставки"""
    def _decorator(fn):
        def wrapper(*args, **kwargs):
            action_time = randint(1, 20)
            if string is not None:
                return string.format(action_time)
            return '{} - {}с!'.format(fn.__name__, action_time)

        return wrapper

    return _decorator


@log('👨‍🍳 Приготовили за {}с!')
def bake():
    """Готовит пиццу"""


@log('🛵 Доставили за {}с!')
def delivery():
    """Доставляет пиццу"""
    pass


@log('🏠 Забрали за {}с!')
def pickup():
    """Самовывоз"""
    pass


if __name__ == '__main__':
    pizza = 'Pizza'  # do not use exemplar due to circular imports
    print(bake(pizza))
    print(delivery(pizza))
    print(pickup(delivery))
