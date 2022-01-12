print("Write how many ml of water the coffee machine has:")
water = int(input())
print("Write how many ml of milk the coffee machine has:")
milk = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
coffee_beans = int(input())
print("Write how many cups of coffee you will need:")
need_cups = int(input())

cups = min(water // 200, milk // 50, coffee_beans // 15)

if cups == need_cups:
    print("Yes, I can make that amount of coffee")
elif cups > need_cups:
    print(f"Yes, I can make that amount of coffee (and even {cups - need_cups} more than that)")
else:
    print(f"No, I can make only {cups} cups of coffee")
