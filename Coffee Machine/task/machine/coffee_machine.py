# initial status of coffee machine
class CoffeeMachine:
    def __init__(self, money, water, milk, coffee_beans, disposable_cups):
        self.money = money
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups

    def status(self):
        print(f'''The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee_beans} of coffee beans
{self.disposable_cups} of disposable cups
{self.money} of money''')

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        coffee = input()
        if coffee == "1":
            self.money += 4
            self.water -= 250
            self.coffee_beans -= 16
            self.disposable_cups -= 1
        elif coffee == "2":
            self.money += 7
            self.water -= 350
            self.milk -= 75
            self.coffee_beans -= 20
            self.disposable_cups -= 1
        elif coffee == "3":
            self.money += 6
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 12
            self.disposable_cups -= 1
        else:
            print("Invalid input!")

    def fill(self):
        print("Write how many ml of water you want to add:")
        self.water += int(input())
        print("Write how many ml of milk you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans you want to add:")
        self.coffee_beans += int(input())
        print("Write how many disposable coffee cups you want to add:")
        self.disposable_cups += int(input())

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def action(self):
        self.status()
        while True:
            print("Write action (buy, fill, take):")
            action = input()
            if action == "buy":
                self.buy()
                break
            elif action == "fill":
                self.fill()
                break
            elif action == "take":
                self.take()
                break
            else:
                print("Invalid input!")
        print()
        self.status()


my_cfe_machine = CoffeeMachine(550, 400, 540, 120, 9)
my_cfe_machine.action()

