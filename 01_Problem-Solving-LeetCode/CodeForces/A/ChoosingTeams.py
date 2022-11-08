__author__ = 'deveshbajpai'
'''
http://codeforces.com/problemset/problem/432/A
Algorithm: Sort the participation list and iterate over it. The step of iteration should be 3 so that in each iteration,
members of a team are considered. Add k to each team's existing participation and check if its lesser than max (ie. 5).
If so increase the team count by 1. Also, take care of the bounds check for team (if it goes beyond list's length)
'''
def solve(n,k,par):
    par = sorted(par)
    teams = 0
    for i in xrange(0,n,3):
        if(i+1<n and i+2<n):
            pl1 = par[i]+k
            pl2 = par[i+1]+k
            pl3 = par[i+2]+k
            if(pl1<=5 and pl2<=5 and pl3<=5):
                teams+=1

    print teams

if __name__ == "__main__":
    n,k = map(int,raw_input().split(" "))
    par = map(int,raw_input().split(" "))
    solve(n,k,par)