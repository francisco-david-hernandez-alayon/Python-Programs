from pizza.ingredient import Ingredient


class IngredientsList:
    # VEGAN
    tomato = Ingredient(name="Tomato", price=0.5, vegan_friendly=True)
    vegan_cheese = Ingredient(name="Vegan Cheese", price=1.5, vegan_friendly=True)
    mushroom = Ingredient(name="Mushroom", price=1.0, vegan_friendly=True)
    olive = Ingredient(name="Olive", price=0.7, vegan_friendly=True)
    onion = Ingredient(name="Onion", price=0.4, vegan_friendly=True)
    pepper = Ingredient(name="Pepper", price=0.6, vegan_friendly=True)

    # NON VEGAN
    cheese = Ingredient(name="Cheese", price=1.2, vegan_friendly=False)
    pepperoni = Ingredient(name="Pepperoni", price=2.0, vegan_friendly=False)
    ham = Ingredient(name="Ham", price=1.8, vegan_friendly=False)
    chicken = Ingredient(name="Chicken", price=2.2, vegan_friendly=False)
    bacon = Ingredient(name="Bacon", price=2.0, vegan_friendly=False)

    @classmethod
    def all(cls):
        return [
            cls.tomato, cls.vegan_cheese, cls.mushroom,
            cls.olive, cls.onion, cls.pepper,
            cls.cheese, cls.pepperoni, cls.ham,
            cls.chicken, cls.bacon
        ]

    @classmethod
    def vegan(cls):
        return [
            cls.tomato, cls.vegan_cheese,
            cls.mushroom, cls.olive,
            cls.onion, cls.pepper
        ]

    @classmethod
    def non_vegan(cls):
        return [
            cls.cheese, cls.pepperoni,
            cls.ham, cls.chicken, cls.bacon
        ]