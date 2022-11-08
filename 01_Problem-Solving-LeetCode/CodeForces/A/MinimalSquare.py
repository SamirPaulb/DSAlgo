__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1360/A

Solution: The rectangles need to be touching each other inorder to use the minimum space. Now the question arises if
they would touch along the height or the width. 

If they touch along the height, then the side of the square should be either 2a or b. We pick the maximum of them to 
make sure it can fit in both sides. Hence max(2a, b)

If they touch along the width, then the side of the square should be either a or 2b. We pick the maximum of them to 
make sure it can fit in both sides. Hence max(a, 2b)

Note: Note that the 2 is due to the 2 rectangles. Had we been dealing with n rectangles, that would be na or nb. 
Since the objective is to minimize the area of the resultant square, we want to have the smaller side of the square. 
So we pick the minimum of the above two alternative. Hence min(max(2a, b), max(a, 2b))

For the area of the resultant square, we raise it to the power of 2. Hence pow(min(max(2a, b), max(a, 2b)), 2)

'''


def solve(a, b):

    return pow(min(max(2*a, b), max(a, 2*b)), 2)


if __name__ == "__main__":
    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        a, b = map(int, raw_input().split(" "))
        results.append(solve(a, b))

    for result in results:
        print result
