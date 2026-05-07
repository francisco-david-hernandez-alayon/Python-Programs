from pydantic import validate_call
from pizza_restaurant import PizzaRestaurant
from simulation_maganer import SimulationManager
from pizza.pizza import Pizza
from pizza.ingredient import Ingredient
from pizza.pizza_list import PizzaList
from pizza.ingredients_list import IngredientsList
import random
import subprocess
import os


CLIENT_BY_PHASE = (4, 8)


# GENERAL PRINT FUNCTIONS
@validate_call
def print_day_brief(restaurant: PizzaRestaurant, simulation: SimulationManager):
    print(f"Day {simulation.currentDay}/{simulation.dayToFinish}")
    print(restaurant)

def clear_screen():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

def PrintIngredientList(ingredients: list[Ingredient]):
    for i, ingredient in enumerate(ingredients):
        print(f"{i}: {ingredient}")

def PrintPizzaList(pizzas: list[Pizza]):
    for i, pizza in enumerate(pizzas):
        print(f"{i}: {pizza}")


# PRINT MENU FUNCTIONS
@validate_call
def preparing_phase_menu(restaurant, simulation):

    while True:
        clear_screen()
        print_day_brief(restaurant=restaurant, simulation=simulation)

        print("\n[PREPARING PHASE MENU]")
        print("[P] See pizza recipes")
        print("[I] Buy ingredient")
        print("[C] Cook pizza")
        print("[E] End preparing phase")

        choice = input("\nChoose option: ").upper()

        # EXIT DAY
        if choice == "E":
            break
        
        # SE PIZZA RECIPES
        elif choice == "P":
            PrintPizzaList(PizzaList.all())

        # BUY INGREDIENT
        elif choice == "I":
            clear_screen()
            print("=== INGREDIENTS ===")
            PrintIngredientList(IngredientsList.all())

            try:
                index = int(input("\nSelect ingredient index: "))
                quantity = int(input("Quantity: "))

                ingredient = IngredientsList.all()[index]

                success = restaurant.buyIngredient(ingredient, quantity)

                if success:
                    print("\nPurchase successful!")
                else:
                    print("\nNot enough money!")

            except (IndexError, ValueError):
                print("\nInvalid selection!")


        # COOK PIZZA
        elif choice == "C":
            clear_screen()
            print("=== PIZZAS ===")
            PrintPizzaList(PizzaList.all())

            try:
                index = int(input("\nSelect pizza index: "))

                pizza = PizzaList.all()[index]

                print(f"Cooking: {pizza}")

                success = restaurant.cook_pizza(pizza_to_cook=pizza)

                if success:
                    print("\nPizza cooked successfully!")
                else:
                    print("\nNot enough ingredients!")

            except (IndexError, ValueError):
                print("\nInvalid selection!")


        else:
            print("\nInvalid option")

        
        input("\n[ENTER TO CONTINUE]")


@validate_call
def client_phase(restaurant, simulation):

    # generate clients
    num_clients = random.randint(*CLIENT_BY_PHASE)

    for i in range(num_clients):
        clear_screen()
        print_day_brief(restaurant=restaurant, simulation=simulation)

        print(f"CLIENT {i+1}/{num_clients}")

        order = simulation.generateClientOrder()

        print(f"\nClient wants: {order.name}")

        # check if have stock
        owned_pizza = None

        for pizza in restaurant.pizzas_stored:
            if pizza.name == order.name:
                owned_pizza = pizza
                break

        if owned_pizza:
            print("You have this pizza!")
            choice = input("Serve it? (Y/N): ").upper()

            if choice == "Y":
                restaurant.sell_pizza(owned_pizza)
                print(F"Pizza served! + {order.price}€")
            else:
                print("Client left unhappy")
                simulation.lostClient()

        else:
            print("You don't have this pizza")
            print("Client left")
            simulation.lostClient()

        input("\n[ENTER TO CONTINUE]")


@validate_call
def end_phase_menu(restaurant, simulation):
    clear_screen()
    print_day_brief(restaurant=restaurant, simulation=simulation)
    simulation.add_day()
    exit = input("\n[ENTER TO CONTINUE] or [E/e to exit]: ")

    if exit == "E" or exit == "e":
        return True
    return False


# GET INIT DATA
print("\n----------INITIALISING PIZZA RESTAURANT SIMULATOR----------\n")
print("Restaurant name: ", end='')
restaurant_name = input()
print("Initial money: ", end='')
initial_money = float(input())
print("Day to Finish: ", end='')
day_to_finish = int(input())


# INIT RESTAURANT
initial_ingredients = [ (1, IngredientsList.cheese), (1, IngredientsList.ham), (1, IngredientsList.tomato) ]
initial_pizzas = [ PizzaList.pizza_hawaiian, PizzaList.pizza_pepperoni, PizzaList.pizza_hawaiian, PizzaList.pizza_pepperoni ]
restaurant = PizzaRestaurant(name=restaurant_name, pizzas_stored=initial_pizzas, ingredients_stored=initial_ingredients, money=initial_money)


# INIT SIMULATION
pizzas_list = PizzaList.all()
ingredients_list = IngredientsList.all()
simulation = SimulationManager(dayToFinish=day_to_finish, pizzas=pizzas_list, ingredients=ingredients_list)


# START SIMULATION
clear_screen()
while not simulation.simulationFinished():
    # PREPARING PHASE PHASE: can buy ingredients and cook Pizzas
    preparing_phase_menu(restaurant=restaurant, simulation=simulation)

    # CLEINT PHASE: can serve clients pizzas cooked and earn money
    client_phase(restaurant=restaurant, simulation=simulation)

    # END DAY PHASE: can continue or exit
    exit = end_phase_menu(restaurant=restaurant, simulation=simulation)
    if exit:
        break

print(f"Simulation Finished:\n* client Lost: {simulation.clientLosts}\n* final money: {restaurant.money}")


