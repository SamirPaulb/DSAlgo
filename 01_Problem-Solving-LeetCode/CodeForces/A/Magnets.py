__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/344/A
Solution: Check every incoming magnet for its left pole with previous right pole. If they
match, increase the count by 1. Check for all magnets and return the value of count.
'''
class Magnets:
    n = 0
    magnets = list()

    def solve(self):
        if(len(self.magnets)==0):
            return 0

        count = 1
        lastPole = self.magnets[0][1]
        for i in range(1,self.n):
            if(self.magnets[i][0]==lastPole):
                count+=1
            lastPole = self.magnets[i][1]

        return count


if __name__ == "__main__":
    m = Magnets()
    m.n = int(raw_input())
    _n = 0
    while _n < m.n:
        m.magnets.append(raw_input())
        _n+=1
    print m.solve()