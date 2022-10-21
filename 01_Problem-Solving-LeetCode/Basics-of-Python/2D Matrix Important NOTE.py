# Python 2D Matrix Important NOTE:

n = 4
a = [[0]*n]*n
#Here every columns are in same line--> NOT a Matrix
for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = 2
print(a) 
#Result = [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]



n = 4
a = [[0]*n for i in range(n)] 
#Here for loop creating the rows in difernt lines--> 2D Matrix
for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = 2
print(a) 
#Retult = [[2, 0, 0, 0], [0, 2, 0, 0], [0, 0, 2, 0], [0, 0, 0, 2]]
