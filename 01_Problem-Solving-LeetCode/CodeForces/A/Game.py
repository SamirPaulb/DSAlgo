__author__ = 'deveshbajpai'
'''
Problem Url: http://codeforces.com/problemset/problem/513/A

Algorithm: Observe the problem requirements closely. Each player, playing optimally will remove 1 ball each time.
The player having larger number of original balls will have more balls, hence more rounds to survive. Hence, values
of k1 and k2 do not matter. If n1 is larger than n2, First player will win. If not, if they are equal or n2 is greater,
the chance will come to first player and he will not have a ball to play, hence he will loose. So, for n2=n1 and n2>n1
cases, second player will win. Nice problem.
'''
def solve(n1,n2):

    if(n1>n2):
        return "First"
    else:
        return "Second"


if __name__ == "__main__":
    n1,n2,k1,k2 = map(int,raw_input().split(" "))
    print solve(n1,n2,k1,k2)