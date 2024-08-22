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
            print(f"Profit {coins.get_profit()}")
        else:
            drink = menu.get_drink(drink)
            make_coffee, missing_resources = coffee_machine.are_resources_enough(drink)
            if make_coffee:
                coins_enough =coins.are_coins_enough(drink)
                if coins_enough:
                    coffee_machine.deduct_resources(drink)
                    print(f"Here is your {drink.name} Enjoy!")


if __name__ == "__main__":
    main()