__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1077/A

Solution: The total distance travelled towards right would be a * k/2. So would be towards left amounting to b * k/2. 
If k is odd, we do an extra move towards right and needs to be added. The difference of right and left net distances is
the final answer.  
'''


def solve(a, b, k):

    dist_right = a * (k/2)
    dist_left = b * (k/2)

    if k % 2 == 1:
        dist_right += a

    return dist_right - dist_left


if __name__ == "__main__":

    t = int(raw_input())

    for _ in xrange(0, t):
        a, b, k = map(int, raw_input().split(" "))
        print solve(a, b, k)
