'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''

n = int(input("Enter number of rows:  "))

row= 1
while row<=n:
    col = 1
    while col<=row:
        print(end="* ")
        col = col +1
    print()
    row = row + 1



