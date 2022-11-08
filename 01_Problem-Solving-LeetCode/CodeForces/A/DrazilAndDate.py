__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/515/A

Solution: The required minimum distance would require a steps in x-axis parallel direction, and b steps in y-axis
parallel direction. If the given steps is lesser than this, the travel is not possible. If the given steps is equal or
more than the required steps, the remainder of those values should be even. This means that even though Drazil reached
(a,b), he went about even steps and came back to it (going and cancelling a step makes it 2 steps, hence the extra
steps should be even).
'''


def solve(a, b, s):

    distReq = abs(a) + abs(b) #abs takes care of negative co-ordinates and still taking positive step-distance

    if distReq > s:
        return "No"
    elif (s - distReq) % 2 == 0:
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    a,b,s = map(int, raw_input().split(" "))
    print solve(a, b, s)
