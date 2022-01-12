print("Write how many cups of coffee you will need:")
cups = int(input())
water = 200 * cups
milk = 50 * cups
coffee_beans = 15 * cups
print(f'''For {cups} cups of coffee you will need:
{water} ml of water
{milk} ml of milk
{coffee_beans} g of coffee beans''')
