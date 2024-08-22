from menu import Menu
class CoffeeMachine:
    def __init__(self):
        self.resources ={
          "water": 300,
          "milk": 200,
          "coffee" : 100
      }
        self.profit = 0
    item = Menu()
    def  get_resources(self):
        items = []
        for resource, quantity in self.resources.items():
            items.append(f"{resource.capitalize}: {quantity}\n")
        return "".join(items)

    def are_resources_enough(self, drink):
        missing_ingredients = []
        menu_drink = self.item.get_drink(drink)
        for resource, quantity in self.resources.items():
            if quantity < menu_drink.ingredients[resource]:
                missing_ingredients.append(resource)
        return len(missing_ingredients) == 0, missing_ingredients



    def get_missing_resources(self, missing_ingredients):
        display_missing = {
            1: "Sorry! There's not enough {}!",
            2: "Sorry! There's not enough {} and {}",
            3: "Sorry! There's not enough {}, {} and {}",
        }
        return display_missing[len(missing_ingredients)].format(*missing_ingredients)

    def deduct_resources(self, drink):
        for ingredient in drink["ingredients"]:
            self.ingredient -= ingredient