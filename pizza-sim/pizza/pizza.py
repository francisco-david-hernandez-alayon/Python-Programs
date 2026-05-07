from pydantic import BaseModel, Field
from pizza.ingredient import Ingredient

class Pizza(BaseModel): 
    name: str = Field(...)
    price: float = Field(...)
    ingredients_needed: list[Ingredient] = Field(...)
    
    def isVegan(self):
        for i in self.ingredients_needed:
            if not i.vegan_friendly:
                return False
        return True
            
    def __str__(self):
        ingredients_text = ", ".join(
            ingredient.name for ingredient in self.ingredients_needed
        )

        vegan_text = " (V)" if self.isVegan() else ""

        return f"Pizza {self.name}{vegan_text} - sell price: {self.price}€ \n   > Ingredients: {ingredients_text}"
    