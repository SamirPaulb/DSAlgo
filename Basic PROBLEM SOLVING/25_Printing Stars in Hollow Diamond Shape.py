'''
  *
 * *
*   *
 * *
  *


# for 5 rows and 5 columns

for row in range(5):
    for col in range(5):
        if row + col ==2 or row - col == 2 or col - row ==2 or col+row ==6:
            print("*",end="")
        else:
            print(end=" ")
    print()

'''

# for 7 rows and 7 columns

for row in range(7):
    for col in range(7):
        if row +col == 3 or row-col==3 or col-row ==3 or row +col==9:
            print("*",end="") 
        else:
            print(end=" ")
    print()



