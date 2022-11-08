'''
http://codeforces.com/problemset/problem/231/A
Solution: The idea is to parse each line of inputs (strings of 0 and 1) and take a count of 1s in it.
It can be done using Counter from collections package. If its >=2, then its a majority in 3 friends. 
Bingo => consider the current problem as solvable. Repeat this for all inputs.
'''
from collections import Counter

class Team:
    def solve(self,n,friendViews):
        solvable = 0
        for friendView in friendViews: 
            if(Counter(friendView)['1']>=2):
                solvable+=1
        
        return solvable
        
if __name__ == "__main__":
    #take inputs
    friendViews = list()
    n = int(raw_input())
    _n = 0
    while(_n<n):
        friendViews.append(raw_input())
        _n+=1
    
    
    t = Team()
    print t.solve(n,friendViews)