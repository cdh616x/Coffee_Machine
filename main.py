from menu import MENU
from resources import resources


def coffee_machine():
    user_input = input("What would you like? (espresso/latte/cappuccino) or options\n")
    while user_input != "off":
        if user_input == "options":
            option = input("Please select one of the following items: refill, capacity, off\n")
            if option == "refill":
                resources["water"] += 300
                resources["milk"] += 200
                resources["coffee"] += 100
                return coffee_machine()
            elif option == "capacity":
                print(resources)
                return coffee_machine()
        elif user_input == "espresso":
            if resources["water"] >= 50 and resources["coffee"] >= 18:
                quarters = input("How many quarters would you like to deposit?\n")
                quarters_total = int(quarters) * .25
                if quarters_total >= (MENU[user_input]["cost"]):
                    resources["water"] -= 50
                    resources["coffee"] -= 18
                    print("Here is your espresso; enjoy!")
                    return coffee_machine()
                else:
                    print("Sorry, but you need more money for that!")
                    return coffee_machine()
            else:
                print("Please refill the machine to make a drink!\n*\n*")
                return coffee_machine()
        elif user_input == "latte":
            if resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24:
                quarters = input("How many quarters would you like to deposit?\n")
                quarters_total = int(quarters) * .25
                if quarters_total >= (MENU[user_input]["cost"]):
                    resources["water"] -= 200
                    resources["milk"] -= 150
                    resources["coffee"] -= 24
                    print("Here is your latte; Enjoy!")
                    return coffee_machine()
                else:
                    print("Sorry, but you need more money for that!")
                    return coffee_machine()
            else:
                print("Please refill the machine to make a drink\n*\n*")
                return coffee_machine()
        elif user_input == "cappuccino":
            if resources["water"] >= 250 and resources["milk"] >= 100 and resources["coffee"] >= 24:
                quarters = input("How many quarters would you like to deposit?\n")
                quarters_total = int(quarters) * .25
                if quarters_total >= (MENU[user_input]["cost"]):
                    resources["water"] -= 250
                    resources["milk"] -= 100
                    resources["coffee"] -= 24
                    print("Here is your cappuccino; Enjoy!")
                    return coffee_machine()
                else:
                    print("Sorry, but you need more money for that!")
                    return coffee_machine()
            else:
                print("Please refill the machine to make a drink\n*\n*")
                return coffee_machine()
        else:
            print("Please select a valid option!")
            return coffee_machine()
        break


coffee_machine()
