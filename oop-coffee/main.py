from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine




def coffee_machine():
    coffee = CoffeeMaker()
    menu = Menu()
    user_input = input("Please select your beverage: " + menu.get_items() + "\n")
    while user_input != "off":
        if user_input == "latte" or "cappuccino" or "espresso":
            drink = menu.find_drink(user_input)
            print("$" + str(drink.cost), drink.name)
            return coffee_machine()
        elif user_input == "refill":
            coffee.resources("water")




# drink = menu.find_drink(user_input)
# print(drink.name)

coffee_machine()