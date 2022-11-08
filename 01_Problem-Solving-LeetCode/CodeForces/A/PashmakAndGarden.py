__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/459/A

Solution: Resolve into 3 cases of given points being on the same vertical, horizontal or diagonal. 
Follow the diagrams and calculate the co-ordinates.  
'''


def solve(x1, y1, x2, y2):

    x_dist = abs(x2 - x1)
    y_dist = abs(y2 - y1)

    if x_dist == 0:

        '''
        * ---- x3,y3
        |
        |
        * ---- x4,y4
        
        '''
        sq_side = y_dist

        x3 = x1 + sq_side
        y3 = min(y1, y2)

        x4 = x1 + sq_side
        y4 = max(y1, y2)

    elif y_dist == 0:

        '''
        * ---------- *
        |
        |
        |
        x3,y3 ---- x4,y4
       
       '''

        sq_side = x_dist

        x3 = min(x1, x2)
        y3 = y1 + sq_side

        x4 = max(x1, x2)
        y4 = y1 + sq_side

    else:

        if x_dist != y_dist:
            return -1
        else:

            '''
            * ---------- x3, y3
            |
            |
            |
            x4,y4 ---------- *
           
            '''

            x3 = x1
            y3 = y2

            x4 = x2
            y4 = y1

    return str(x3) + " " + str(y3) + " " + str(x4) + " " + str(y4)


if __name__ == "__main__":

    x1, y1, x2, y2  = map(int, raw_input().split(" "))
    print solve(x1, y1, x2, y2)
