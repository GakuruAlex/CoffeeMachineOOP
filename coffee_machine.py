class CoffeeMachine:
    def __init__(self):
        self.water = 300
        self.milk = 200
        self.coffee = 100
        self.profit = 0
    
    def  get_resources(self):
        return f"Water: {self.water}\nMilk: {self.milk}\nCoffee: {self.coffee}"