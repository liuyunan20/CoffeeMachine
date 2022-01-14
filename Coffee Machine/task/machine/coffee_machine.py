# initial status of coffee machine
class CoffeeMachine:
    def __init__(self, money, water, milk, coffee_beans, disposable_cups):
        self.money = money
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.exit_all = False

    def status(self):
        print(f'''The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee_beans} of coffee beans
{self.disposable_cups} of disposable cups
${self.money} of money''')

    def check_resource(self, coffee):
        enough_resource = False
        if coffee == "1":
            # check if enough for espresso
            if self.water < 250:
                print("Sorry, not enough water!")
            if self.coffee_beans < 16:
                print("Sorry, not enough coffee beans!")
            if self.disposable_cups == 0:
                print("Sorry, not enough disposable cups!")
            if self.water >= 250 and self.coffee_beans >= 16 and self.disposable_cups >= 1:
                print("I have enough resources, making you a coffee!")
                enough_resource = True

        elif coffee == "2":
            # check if enough for latte
            if self.water < 350:
                print("Sorry, not enough water!")
            if self.milk < 75:
                print("Sorry, not enough milk!")
            if self.coffee_beans < 20:
                print("Sorry, not enough coffee beans!")
            if self.disposable_cups == 0:
                print("Sorry, not enough disposable cups!")
            if self.water >= 350 and self.milk >= 75 and self.coffee_beans >= 20 and self.disposable_cups >= 1:
                print("I have enough resources, making you a coffee!")
                enough_resource = True

        elif coffee == "3":
            # check if enough for latte
            if self.water < 200:
                print("Sorry, not enough water!")
            if self.milk < 100:
                print("Sorry, not enough milk!")
            if self.coffee_beans < 12:
                print("Sorry, not enough coffee beans!")
            if self.disposable_cups == 0:
                print("Sorry, not enough disposable cups!")
            if self.water >= 200 and self.milk >= 100 and self.coffee_beans >= 12 and self.disposable_cups >= 1:
                print("I have enough resources, making you a coffee!")
                enough_resource = True
        return enough_resource

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee = input()
        if coffee == "back":
            self.action()
        elif self.check_resource(coffee):
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

    def exit(self):
        self.exit_all = True

    def action(self):
        while True:
            print("Write action (buy, fill, take, remaining, exit):")
            action = input()
            if action == "buy":
                print()
                self.buy()
                print()

            elif action == "fill":
                print()
                self.fill()
                print()

            elif action == "take":
                print()
                self.take()
                print()

            elif action == "remaining":
                print()
                self.status()
                print()

            elif action == "exit":
                self.exit()
            else:
                print("Invalid input!")
            if self.exit_all:
                break


my_cfe_machine = CoffeeMachine(550, 400, 540, 120, 9)
my_cfe_machine.action()

