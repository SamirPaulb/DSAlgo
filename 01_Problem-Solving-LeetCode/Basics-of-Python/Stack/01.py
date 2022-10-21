stack = []

def push():
    elment = input("Write a number here: \n")
    stack.append(elment)
    print(stack)

def pop_element():
    if not stack:
        print("The stack is Empty")
    else:
        e = stack.pop()
        print("Element removed: \n",e)
        print(stack)

while True:
    #print("Choose a option from here:   1.Push, 2.Pop,  3.Quit")
    a = int(input("Choose a option from here:   1.Push, 2.Pop,  3.Quit \n"))
    if a == 1:
        push()
    elif a ==2 :
        pop_element()
    elif a == 3:
        break
    else:
        print("Enter the correct option")

   