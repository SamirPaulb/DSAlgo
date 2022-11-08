__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1337/A

Solution: Use b, c and c to get the triangle inequalities satisfied. 


'''

if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        a, b, c, d = map(int, raw_input().split(" "))
        print str(b) + " " + str(c) + " " + str(c)
