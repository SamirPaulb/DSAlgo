__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1301/A

Solution: Iterate over the strings (since they're of equal lengths, just run a loop of any of a,b or c's length.
Since we need to swap a character of string a or b at ith position with that of c, we need to check the following 
condition: if a[i] != c[i] and b[i] != c[i]. 
If this is true, it means we cannot swap either a or b and hence we will have this as a different character in a and b.
Hence return NO. If we cannot satisfy the condition all positions, the strings a and b can be made same and hence return
YES.

Time Complexity: O(n)
'''


def solve(a, b, c):

    l = len(a) #a, b and c are of equal length

    for i in xrange(0, l):

        if a[i] != c[i] and b[i] != c[i]:
                return "NO"

    return "YES"


if __name__ == "__main__":
    n = int(raw_input())

    answers = []
    for i in xrange(0,n):
        a = raw_input()
        b = raw_input()
        c = raw_input()
        answers.append(solve(a, b, c))

    for answer in answers:
        print answer
