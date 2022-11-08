__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/510/A

Solution: The rows have pattern for even and odd indexed ones. For the former, it has all cells with snake body, 
while the later as alternating empty cells with right/left aligned snake body. Keep track of that with a boolean flag.  
'''


def solve(n, m):

    snakeBody = "#"
    snakeBodies = snakeBody * m
    emptyCells = "." * (m-1)

    # flag denotes if the snake body on the right or the left side for alternate rows
    isRight = True

    for row in xrange(0, n):

        if row % 2 == 0:
            print snakeBodies
        else:
            if isRight:
                print emptyCells + snakeBody
            else:
                print snakeBody + emptyCells
            # toggle it
            isRight = not isRight


if __name__ == "__main__":

    n, m = map(int, raw_input().split(" "))

    solve(n, m)
