try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
    exit()
finally:
    print("We are done")

print("Thanks for using the program")