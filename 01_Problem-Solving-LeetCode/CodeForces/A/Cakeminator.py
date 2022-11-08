__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/330/A
Algorithm: First check in columns to found edible columns. Track if there is ateast one available cake and no evil strawberry
in that column. If so, add it in a list. Do similar for the rows. Only difference is, keep track of available cake pieces in
each row (exclude the eaten cakes in the columns earlier). In the end, return the total cakes eaten in column + that in rows.
'''
def solve(r,c,cake):
    #check columns without evil strawberry and atleast one normal cake
    col = list()
    for i in range(0,c):
        isColEdible = True
        isOneCakeAvailable = False
        for j in range(0,r):
            if(cake[j][i]=="."):
                isOneCakeAvailable = True
            elif(cake[j][i]=="S"):
                isColEdible = False

        if(isOneCakeAvailable and isColEdible):
            col.append(i)

    #print "cols edible ",col

    #check rows without evil strawberry and atleast one normal cake
    row = list()
    allRowsEdibleCount = 0
    for i in range(0,r):
        thisRowEdibleCount = 0
        isRowEdible = True
        isOneCakeAvailable = False
        for j in range(0,c):
            if(cake[i][j]=="." and j not in col):
                isOneCakeAvailable = True
                thisRowEdibleCount+=1
            elif(cake[i][j]=="S"):
                isRowEdible = False

        if(isOneCakeAvailable and isRowEdible):
            row.append(i)
            allRowsEdibleCount += thisRowEdibleCount

    #print "rows edible ",row

    return len(col)*r + allRowsEdibleCount


if __name__ == "__main__":
    r,c = map(int,raw_input().split(" "))
    cake = list()
    _r = 0
    while(_r < r):
        cake_line = list()
        cake_line = raw_input()
        cake.append(cake_line)
        _r+=1

    print solve(r,c,cake)
