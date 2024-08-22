class CoffeeMachine:
    def __init__(self):
        self.water = 300
        self.milk = 200
        self.coffee = 100
        self.profit = 0

    def  get_resources(self):
        return f"Water: {self.water}\nMilk: {self.milk}\nCoffee: {self.coffee}"

    def are_resources_enough(self, drink):
        missing_ingredients = []

        for ingredient in drink["ingredients"]:
            if self.ingredient < drink["ingredient"]:
                missing_ingredients.append(ingredient)

        return len(missing_ingredients) == 0 , missing_ingredients

    def get_missing_resources(self, missing_ingredients):
        display_missing = {
            1: "Sorry! There's not enough {}!",
            2: "Sorry! There's not enough {} and {}",
            3: "Sorry! There's not enough {}, {} and {}",
        }
        return display_missing[len(missing_ingredients)].format(*missing_ingredients)

    def add_profit(self, drink):
        self.profit += drink["cost"]
        return self.profit