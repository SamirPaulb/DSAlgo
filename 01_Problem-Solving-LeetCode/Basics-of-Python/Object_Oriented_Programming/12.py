expense = [2200, 2350, 2600, 2130, 2190]

print(expense[1] - expense[0])
print(expense[0]+expense[1]+expense[2])

print("did I spend $2000 in any month? ", 2000 in expense)

expense.append(1980)
print(f"I spend ${expense[5]} in june")

expense[3] = 1930
print(expense)
