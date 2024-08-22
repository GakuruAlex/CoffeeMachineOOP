from coins_machine import Coins
from coffee_machine import CoffeeMachine
from menu import Menu, MenuItem

def main():
    coins = Coins()
    coffee_machine = CoffeeMachine()
    menu = Menu()
    is_on = True
    while is_on:
        drink = input(f"Menu item : {menu.get_menu_items()}: ").lower()

        if drink == "end":
            break
        elif drink == "report":
            print(coffee_machine.get_resources())

if __name__ == "__main__":
    main()