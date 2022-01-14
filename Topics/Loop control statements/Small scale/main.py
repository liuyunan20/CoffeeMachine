nums = []
while True:
    num = input()
    if num == ".":
        break
    else:
        nums.append(float(num))
print(min(*nums))
