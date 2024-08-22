class Coins:
    profit = 0
    COINS = {
        "quarter":0.25,
        "dime":0.10,
        "nickel":0.05,
        "penny":0.01,
    }
    def ask_for_coins(self):
        for coin in self.COINS:
            coins_total += int(input(f"Please insert number of {coin}: ")) * self.COINS[coin]
        return coins_total
    def are_coins_enough(self, drink):
        coins =self.ask_for_coins()
        
        if coins >= drink["cost"]:
            change =coins - drink["cost"]
            print(f"Here is {change} in change")
            return True
        print("Money not enough. Money refunded")