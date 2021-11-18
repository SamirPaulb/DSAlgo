'''
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''

n = int(input("type the number:  "))
for row in range(1,n+1):
    for col in range(1,n+2-row):
        print(col, end=" ")
    print()

