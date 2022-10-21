a = 54 # Global variable
def func1():
    global a
    print(f"Print statement 1: {a}")
    a = 8 # Local Variable if global keyword is not used
    print(f"Print statement 2: {a}")

func1()
print(f"Print statement 3: {a}")