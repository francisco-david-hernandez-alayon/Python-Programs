from pydantic import BaseModel, Field, validate_call
from pizza.pizza import Pizza
from pizza.ingredient import Ingredient

class PizzaRestaurant(BaseModel):
    name: str = Field(...)
    money: float = 0
    pizzas_stored: list[Pizza] = Field(...)
    ingredients_stored: list[tuple[int, Ingredient]] = Field(...) # (quantity, ingredient)

    @validate_call
    def buyIngredient(self, ingredient: Ingredient, quantity: int = 1) -> bool:
        total_cost = ingredient.price * quantity

        # Check if restaurant can afford it
        if self.money < total_cost:
            return False

        # Search if ingredient already exists
        for i, (qty, stored_ingredient) in enumerate(self.ingredients_stored):
            if stored_ingredient.name == ingredient.name:
                # update quantity
                self.ingredients_stored[i] = (
                    qty + quantity,
                    stored_ingredient
                )

                self.money -= total_cost
                return True

        # if not exist, add new one
        self.ingredients_stored.append((quantity, ingredient))
        self.money -= total_cost

        return True

    @validate_call
    def cook_pizza(self, pizza_to_cook: Pizza):
        new_stock = self.ingredients_stored.copy()

        for needed_ingredient in pizza_to_cook.ingredients_needed:

            # search ingredient int stock
            stock_item = next(
                (
                    item
                    for item in new_stock
                    if item[1].name == needed_ingredient.name
                ),
                None
            )

            # no stock available for item
            if stock_item is None:
                return False

            quantity, ingredient = stock_item
            if quantity <= 0:
                return False

            # remove old tuple add updated quantity for stock
            new_stock.remove(stock_item)
            if quantity - 1 > 0:
                new_stock.append(
                    (quantity - 1, ingredient)
                )

        self.ingredients_stored = new_stock # update current stock
        self.pizzas_stored.append(pizza_to_cook)
        return True

    @validate_call
    def sell_pizza(self, pizza_to_sell: Pizza):
        # check if there is pizza to sell
        pizza_sell = next(
                (
                    pizza
                    for pizza in self.pizzas_stored
                    if pizza.name == pizza_to_sell.name
                ),
                None
            )
        if pizza_sell is None:
                return False

        self.pizzas_stored.remove(pizza_sell)

        self.money += pizza_to_sell.price
        return True
        

    def __str__(self) -> str:
        ingredients_text = ""

        for quantity, ingredient in self.ingredients_stored:
            ingredients_text += f"\n        - {ingredient.name} x{quantity}"

        pizzas_text = ""

        for pizza in self.pizzas_stored:
            pizzas_text += f"\n     - {pizza.name}"

        return (
            f"Restaurant {self.name} ({self.money}€)\n"
            f"  > Pizzas:{pizzas_text}\n"
            f"  > Ingredients:{ingredients_text}\n"
        )