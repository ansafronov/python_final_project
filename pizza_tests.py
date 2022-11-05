import unittest

from pizza import Pizza, Margherita, Hawaiian, Pepperoni, Order
from click.testing import CliRunner
from cli import my_cli


class MyTestCase(unittest.TestCase):
    def test_Pizza_class(self):
        pizza = Pizza(
            'Mushrooms Pizza',
            ['Tomato sauce', 'mozzarella', 'mushrooms']
        )
        self.assertEqual(pizza.name, 'Mushrooms Pizza')
        self.assertEqual(
            pizza.ingredients,
            ['Tomato sauce', 'mozzarella', 'mushrooms']
        )
        self.assertEqual(pizza.size, 'L')

    def test_Pizza_class_size(self):
        with self.assertRaises(ValueError):
            Pizza('Mushrooms Pizza',
                  ['Tomato sauce', 'mozzarella', 'mushrooms'], size='M'
                  )

    def test_Pizza_class_dict(self):
        pizza = Pizza('Mushrooms Pizza',
                      ['Tomato sauce', 'mozzarella', 'mushrooms'])
        self.assertEqual(
            pizza.dict(),
            {'Mushrooms Pizza': ['Tomato sauce', 'mozzarella', 'mushrooms']}
        )

    def test_Pizza_Margherita_str(self):
        pizza = Margherita()
        self.assertEqual(str(pizza), pizza.name + ' 🧀')

    def test_Pizza_Pepperoni_str(self):
        pizza = Pepperoni()
        self.assertEqual(str(pizza), pizza.name + ' 🍕')

    def test_Pizza_Hawaiian_str(self):
        pizza = Hawaiian()
        self.assertEqual(str(pizza), pizza.name + ' 🍍')

    def test_Order(self):
        pizza = Margherita()
        order = Order(pizza)
        self.assertEqual(order.is_baked, 0)
        self.assertEqual(order.is_delivered, 0)

        bake_message = order.bake()
        self.assertEqual(order.is_baked, 1)
        self.assertEqual(bake_message[:19], '👨‍🍳 Приготовили за ')
        self.assertEqual(bake_message[-2:], 'с!')

        deliver_message = order.deliver()
        self.assertEqual(order.is_delivered, 1)
        self.assertEqual(deliver_message[:15], '🛵 Доставили за ')
        self.assertEqual(deliver_message[-2:], 'с!')

    def test_CLI(self):
        runner = CliRunner()
        result = runner.invoke(my_cli, ['menu'])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(
            result.output,
            '''Pepperoni 🍕: tomato sauce, mozzarella, pepperoni
Margherita 🧀: tomato sauce, mozzarella, tomatoes
Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples
'''
        )


if __name__ == '__main__':
    unittest.main()
