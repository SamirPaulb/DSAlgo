word = "python"
a = list(word)
for row in range(len(a)+1):
    for col in range(row+1):
        print(a[col],end="")
    print()


