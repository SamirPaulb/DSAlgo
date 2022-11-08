__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1461/A

Solution: Since we can have a k length substring which should be a palindrome, we start the final string with k 'a's. 
Post that, we need n-k characters more to build the final string. But since we want to break the palindrome in any sub
strings formed with the first k 'a's, we rotate over a list of 'b', 'c' and 'a' (in that order). Finally, return the 
answer as a string.  
'''


def solve(n, k):

    ans = list()
    for i in xrange(0, k):
        ans.append('a')

    other_chars = ['b', 'c', 'a']
    for i in xrange(0, (n-k)):
        ans.append(other_chars[i % 3])

    return "".join(ans)


if __name__ == "__main__":

    t = int(raw_input())

    for _ in xrange(0, t):
        n, k = map(int, raw_input().split(" "))
        print solve(n, k)
