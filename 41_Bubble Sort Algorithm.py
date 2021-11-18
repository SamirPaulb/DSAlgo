n = int(input("How many number you want in the list: "))
a = [int(input("Enter an element to add in the list: ")) for i in range(n) ]


print(a)

for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
       #print(a)  ----->>> to print each steps of sorting
    #print()
print(f"The final sorted list in increasing order is:  {a}")



