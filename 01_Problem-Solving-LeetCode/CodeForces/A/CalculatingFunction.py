__author__ = 'deveshbajpai'
'''
Problem Url: http://codeforces.com/problemset/problem/486/A

Algorithm: Observe the series closely. Since every number is differently signed that its neighbors, the sum
 increases only 1 by every 2 numbers in that series. So, if n is even, the sum would be half of it. If odd, get the
 sum till its previous number which was even, which would be half of it. Now, add the negative n to it since all
 odd numbers are negatively signed in this series. Return the result from both if-else blocks.
'''
def solve(n):
    if(n%2==0):
        return n/2
    else:
        prev = (n-1)/2
        return prev-n


if __name__ == "__main__":
    n = input()
    print solve(n)
