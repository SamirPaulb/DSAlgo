__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/282/A

Solution: If there is a plus sign in the operation, the value would be incremented, otherwise it should have a minus
and would be decremented. The post or prefix doesn't matter since every line as one operation.
'''


if __name__ == "__main__":

    n = int(raw_input())

    value = 0
    for _ in xrange(0, n):
        operation = raw_input()

        if "+" in operation:
            value += 1
        else:
            value -= 1

    print value

