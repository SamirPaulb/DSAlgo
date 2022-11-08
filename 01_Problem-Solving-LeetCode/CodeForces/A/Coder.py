__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/384/A
Algorithm: Seggregate the input into 2 cases: n being odd or not. Follow the code for 2 cases.
'''

# build the grid when n is even
def evenGrid(n):
    result = list()
    cur1 = ""
    cur2 = ""
    for i in range(0,n,2):
        cur1+="C."
    for i in range(0,n,2):
        cur2+=".C"
    for i in range(0,n,2):
        result.append(cur1)
        result.append(cur2)

    return result

# build the grid when n is odd
def oddGrid(n):
    result = list()
    cur1 = ""
    cur2 = ""
    for i in range(0,n,2):
        cur1+="C."
    cur1 = cur1[:-1]
    for i in range(0,n,2):
        cur2+=".C"
    cur2 = cur2[:-1]
    for i in range(0,n,2):
        result.append(cur1)
        result.append(cur2)
    del result[-1]
    return result


# calculate the total pieces based on n being odd or not
def solve(n):
    result = ()
    if(n%2==0):
        result = evenGrid(n)
        print (n/2) * n
    else:
        result = oddGrid(n)
        print ((n/2)+1)*((n/2)+1) + (n/2)*(n/2)

    for i in range(0,len(result)):
        print result[i]

if __name__ == "__main__":
    n = int(raw_input())
    solve(n)


    #reference grids
    '''
    CASE 1: n is even (4)
    c.c.
    .c.c
    c.c.
    .c.c
    '''

    '''
    CASE 2: n is odd (5)
    c.c.c
    .c.c.
    c.c.c
    .c.c.
    c.c.c
    '''