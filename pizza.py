from __future__ import annotations

from typing import List, Dict
from process import bake, delivery


class Pizza:
    def __init__(self, name: str, ingredients: List[str], size: str = 'L'):
        """
        Общий класс для всех пицц

        Parameters
        ----------
        name : str
            Название пиццы.

        ingredients : List[str]
            Ингредиенты в пицце в виде списка.

        size : str
            Размеры пиццы. Может быть 'L' или 'XL'. Дефолтное значени 'L'
        """
        self.appropriate_pizza_sizes = ['L', 'XL']
        if size not in self.appropriate_pizza_sizes:
            raise ValueError(
                'Size of pizza is not in {}'.format(
                    self.appropriate_pizza_sizes
                )
            )

        self.name = name
        self.ingredients = ingredients
        self.size = size

    def dict(self) -> Dict[str, list]:
        """
        Возвращает ингридиенты в виде словаря
        """
        return {self.name: self.ingredients}

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Pizza):
            return NotImplemented
        return self.name == other.name


class Margherita(Pizza):
    def __init__(self):
        """
        Класс для пиццы Margherita
        Рецепт: 'tomato sauce', 'mozzarella', 'tomatoes'
        """
        super().__init__(
            'Margherita',
            ['tomato sauce', 'mozzarella', 'tomatoes']
        )

    def __str__(self):
        return 'Margherita 🧀'


class Pepperoni(Pizza):
    def __init__(self):
        """
        Класс для пиццы Pepperoni
        Рецепт: 'tomato sauce', 'mozzarella', 'pepperoni'
        """
        super().__init__(
            'Pepperoni',
            ['tomato sauce', 'mozzarella', 'pepperoni']
        )

    def __str__(self):
        return 'Pepperoni 🍕'


class Hawaiian(Pizza):
    def __init__(self):
        """
        Класс для пиццы Hawaiian
        Рецепт: 'tomato sauce', 'mozzarella', 'chicken', 'pineapples'
        """
        super().__init__(
            'Hawaiian',
            ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
        )

    def __str__(self):
        return 'Hawaiian 🍍'


class Order:
    def __init__(self,  pizza: Pizza):
        """
        Класс сущности заказа
        Хранит пармерты is_baked и is_delivered.

        Parameters
        ----------
        pizza : Pizza
            Экземпляр пиццы
        """
        self.pizza = pizza

        self.is_baked = 0
        self.is_delivered = 0

    def bake(self):
        """Готовит пиццу в рамках заказа"""
        self.is_baked = 1
        return bake(self.pizza)

    def deliver(self):
        """Доставляет пиццу в рамках заказа"""
        self.is_delivered = 1
        return delivery(self.pizza)
