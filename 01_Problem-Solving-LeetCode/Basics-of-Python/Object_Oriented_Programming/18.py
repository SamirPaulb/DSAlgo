'''
Create a list of all odd numbers between 1 and a max number.
 Max number is something you need to take from a user using input() function
'''

a= int(input("Write the maximum number here: "))

odd_numbers = []

if a%2 !=0 :
    m = (a+1)/2
    for i in range(m):
        j = 2*i + 1
        odd_numbers.append(j)
else:
    n = int(a/2)
    for i in range(n):
        j = 2*i + 1
        odd_numbers.append(j)

print(odd_numbers)


