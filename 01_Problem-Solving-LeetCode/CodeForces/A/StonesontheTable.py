'''
http://codeforces.com/problemset/problem/266/A
Solution: Iterate over the stone list from 1 to length of list and keep checking current element 
with previous element. If same, it needs to be changed.
'''

class StonesontheTable:
    
    def solve(self,n,stones):
        changes = 0
        for i in range(1,n):
            if(stones[i]==stones[i-1]):
                changes+=1    
                    
        return changes

if __name__ == "__main__":
    n = int(raw_input())
    stones = raw_input()
    s = StonesontheTable()
    print s.solve(n,stones)