__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/322/A
Solution: Create combinations with 1 and then with 2. Iterate over m for combinations with 1
and then over n for combinations with 2.
'''
class CielandDancing:
    n = 0
    m = 0
    def solve(self):
        print self.n + self.m - 1
        for i in range(1,self.m+1):
            print 1," ",i
        for i in range(2,self.n+1):
            print i," ",1


if __name__ == "__main__":
    c = CielandDancing()
    c.n,c.m = map(int,raw_input().split(" "))
    c.solve()
