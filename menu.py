class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }
        self.cost = cost
    def __str__(self):
        return self.name

class Menu:
    def __init__(self):
        self.menu_items = [
                    MenuItem(name= "latte", milk= 150, water = 200, coffee = 24, cost = 2.5),
                    MenuItem(name = "espresso", water = 50, coffee = 18, cost = 1.5, milk = 0 ),
                    MenuItem(name = "cappuccino", milk = 100, water = 250, coffee = 24, cost = 3),
        ]

    def get_menu_items(self):
        menu = []
        for item in self.menu_items:
            menu.append(item.name)
        return "/".join(menu)
    def get_drink(self, drink):
        for item in self.menu_items:
            if item.name == drink:
                return item
        return "Drink not Found"