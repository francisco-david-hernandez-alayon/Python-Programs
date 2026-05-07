from pizza.pizza import Pizza
from pizza.ingredients_list import IngredientsList as I


class PizzaList:

    pizza_vegan_delight = Pizza(
        name="Vegan Delight",
        price=11.5,
        ingredients_needed=[
            I.tomato,
            I.vegan_cheese,
            I.mushroom,
            I.onion
        ]
    )

    pizza_green_garden = Pizza(
        name="Green Garden",
        price=10.0,
        ingredients_needed=[
            I.tomato,
            I.olive,
            I.pepper,
            I.mushroom
        ]
    )

    pizza_pepperoni = Pizza(
        name="Pepperoni",
        price=13.0,
        ingredients_needed=[
            I.tomato,
            I.cheese,
            I.pepperoni
        ]
    )

    pizza_hawaiian = Pizza(
        name="Hawaiian",
        price=12.5,
        ingredients_needed=[
            I.tomato,
            I.cheese,
            I.ham
        ]
    )

    pizza_bbq_chicken = Pizza(
        name="BBQ Chicken",
        price=14.0,
        ingredients_needed=[
            I.tomato,
            I.cheese,
            I.chicken,
            I.bacon
        ]
    )

    @classmethod
    def all(cls):
        return [
            cls.pizza_vegan_delight,
            cls.pizza_green_garden,
            cls.pizza_pepperoni,
            cls.pizza_hawaiian,
            cls.pizza_bbq_chicken
        ]

    @classmethod
    def vegan(cls):
        return [
            cls.pizza_vegan_delight,
            cls.pizza_green_garden
        ]

    @classmethod
    def non_vegan(cls):
        return [
            cls.pizza_pepperoni,
            cls.pizza_hawaiian,
            cls.pizza_bbq_chicken
        ]