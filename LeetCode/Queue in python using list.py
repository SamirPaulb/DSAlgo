q = []
def enque(val):
    q.append(val)

def dque(val):
    d = q.pop(0)
    print(d)

def show(q):
    print(q)

while True:
    a = int(input("Enter 1.enque, 2.deque, 3.show, 4.Quit :  "))
    if a == 1:
        val = input("enque:  ")
        enque(val)
    elif a == 2:
        dque(val)
    elif a == 3:
        show(q)
    elif a == 4:
        print("You have successfully quited!")
        break
    else:
        print("Enter a value from 1 to 4.")
