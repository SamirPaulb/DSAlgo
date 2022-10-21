n = int(input("Type a Natural number: \n"))
i = 1
if n>0:
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    print(sum)
else:
    print("Type Natural numbers only")

    