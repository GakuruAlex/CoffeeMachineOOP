class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }
        self.cost = cost

class Menu:
    def __init__(self):
        self.menu = [
                    MenuItem(name= "latte", milk= 150, water = 200, coffee = 24, cost = 2.5),
                    MenuItem(name = "espresso", water = 50, coffee = 18, cost = 1.5, milk = 0 ),
                    MenuItem(name = "cappuccino", milk = 100, water = 250, coffee = 24, cost = 3),
        ]
    def get_menu(self):
        return "".join(self.menu["name"])
    