from pydantic import BaseModel, Field

class Ingredient(BaseModel): 
    name: str = Field(...)
    price: float = Field(...)
    vegan_friendly: bool = Field(...)


    def __str__(self):
        return f"({self.name}, {self.price}€)"