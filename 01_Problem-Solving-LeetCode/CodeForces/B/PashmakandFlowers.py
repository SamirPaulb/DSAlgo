__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/459/B
Solution: Find the max and min elements in the b list. Also, find the frequency of max and
min element. The multiplication is the total number of combinations possible. The difference
of max and min element is the difference required.
A special case needs to be checked when the max and min elements are the same. In that case,
the same number would be counted in both max and min element frequency. If this occurs,
take the sqrt of the count of either maxelem of min elem. Count the number of ways for it
by doing n*n-1 /2 .
'''

class PashmakandFlowers:
    n = 0
    b = list()
    maxDiff = 0
    options = 0

    def solve(self):
        maxElem = self.b[0]
        maxElemCount = 1
        minElem = self.b[0]
        minElemCount = 1
        #find the max and min elements. Also update the max and min element's frequency
        for i in range(1,len(self.b)):
            if(self.b[i] > maxElem):
                maxElem = self.b[i]
                maxElemCount  = 1
            elif(self.b[i] == maxElem):
                maxElemCount+=1

            if(self.b[i] < minElem):
                minElem = self.b[i]
                minElemCount = 1
            elif(self.b[i] == minElem):
                minElemCount +=1


        self.maxDiff = maxElem-minElem
        self.options = maxElemCount*minElemCount
        #special case: when max and min elements are the same
        if(self.maxDiff==0):
            import math
            val = math.sqrt(self.options)
            self.options = int(((val)*(val-1))/2)


if __name__ == "__main__":
    pf = PashmakandFlowers()
    pf.n = int(raw_input())
    pf.b = map(int,raw_input().split(" "))
    pf.solve()
    print pf.maxDiff,pf.options