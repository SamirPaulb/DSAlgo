# Recursive fuction 

def feb(n):
    if n<=1:
        return n
    return feb(n-1) + feb(n-2)

k = int(input(f"k =  "))

for i in range(k):
    print(feb(i))



# Iterativr method for Fibonacci

a = 0
b = 1
n = int(input())
print(a)
print(b)
for i in range(n-2):
    c = a+b
    a,b = b,c
    print(c)


    