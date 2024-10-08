from menu import Menu
class Coins:
    menu = Menu()
    profit = 0
    COINS = {
        "quarter":0.25,
        "dime":0.10,
        "nickel":0.05,
        "penny":0.01,
    }
    def ask_for_coins(self):
        coins_total = 0
        for coin in self.COINS:
            coins_total += int(input(f"Please insert number of {coin}: ")) * self.COINS[coin]
        return coins_total

    def are_coins_enough(self, drink):
        print(f"{drink} cost: ${drink.cost}")
        coins =self.ask_for_coins()
        print(f"You gave: ${coins}")
        if coins >= drink.cost:
            change = round(coins - drink.cost, 2)
            print(f"Here is ${change} in change")
            self.profit += drink.cost
            return True
        return False

    def get_profit(self):
        return self.profit