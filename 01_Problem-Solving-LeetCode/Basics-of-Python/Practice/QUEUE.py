queue = []

def enqueue():
    element = int(input("Write the number to enqueue: \n" ))
    queue.append(element)
    print(f"{element} has been added to the Queue")

def dequeue():
    if not queue:
        print("The queue is empty so can not be dequeued")
    else:
        e = queue.pop(0)
        print("Removed element is: ",e)

def display():
    print(queue)

while True:
    a = int(input('''Choose a option from the following:
    1. enqueue
    2. dequeue
    3. display
    4. quit  \n'''))
    if a==1:
        enqueue()
    elif a==2:
        dequeue()
    elif a==3:
        display()
    elif a==4:
        break
    else:
        print("Choose a correct option")







