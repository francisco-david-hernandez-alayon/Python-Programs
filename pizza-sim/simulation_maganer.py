from pydantic import BaseModel, Field, ConfigDict, validate_call
from pizza.pizza import Pizza
from pizza.ingredient import Ingredient
import random

class SimulationManager(BaseModel):
    currentDay: int = 0
    dayToFinish: int = Field(...)
    clientLosts: int = 0

    pizzas: list[Pizza] = Field(..., frozen=True)
    ingredients: list[Ingredient] = Field(..., frozen=True)


    # Add day and return True if simulation have finished
    def add_day(self):
        self.currentDay += 1
    
    def simulationFinished(self): 
        if self.currentDay >= self.dayToFinish:
            return True
        else:
            return False
        
    def lostClient(self):
        self.clientLosts += 1
        
    def generateClientOrder(self):
        randomPizzaPos = random.randint(0, len(self.pizzas) - 1)
        return self.pizzas[randomPizzaPos]

