'''
n = int(input("Enter a numbre:  "))
num = n
result = 0

while n != 0 :
    result = n%10 +result
    n = n//10

print(f"Sum of each digits of the number {num} is = {result}")

'''


n = input("Enter a numbre:  ")

result = 0

for i in range(len(n)):
    result = int(n[i:i+1]) + result 

print(f"Sum of each digits of the number {n} is = {result}")


