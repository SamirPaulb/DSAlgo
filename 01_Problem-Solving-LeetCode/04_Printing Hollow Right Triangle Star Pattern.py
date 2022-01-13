'''
*
**
* *
*  *
*   *
*    *
*     *
*      *
*       *
**********
'''
n = int(input("Write the number: \n"))

for row in range(n+1):
    for col in range(n+1):
        if row ==n or col ==0 or row ==col:
            print("*", end="")
        else:
            print(end=" ")
    print()


