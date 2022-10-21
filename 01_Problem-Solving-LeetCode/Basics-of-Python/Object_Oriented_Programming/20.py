'''
Create a list of all odd numbers between 1 and a max number.
 Max number is something you need to take from a user using input() function
'''

a = int(input("Write the number here: \n"))

ood_num = []
even_num = []

for i in range(1,a+1):
    if i%2 !=0:
        ood_num.append(i)
    else:
        even_num.append(i)

print("the list of odd number is:  ",ood_num)
print("the list of even number is:  ",even_num)



