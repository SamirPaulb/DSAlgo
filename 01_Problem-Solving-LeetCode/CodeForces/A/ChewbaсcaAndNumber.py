__author__ = 'deveshbajpai'
'''
Problem Url: http://codeforces.com/problemset/problem/514/A
Algorithm: Iterate over number from back, extract the digit, and add the minimum of it and 9-digit to the new number.
After this loop, we have the reverse of required number. Reverse the list. Now, a special check for the first digit
of the new number. If the original number had 9 at it, it would have been 0 in the new number. Restore that. Return
the new number.
'''
def solve(n):
    digit = 0
    new_n = []
    while(n>0):
        digit = n%10
        new_n.append(str(min(digit,9-digit)))
        n /= 10

    new_n.reverse()
    #to check the first digit is not turned into 0 by the above logic
    #that would have happened if the first digit was 9.
    if(digit==9):
        new_n[0] = "9"
    return ''.join(new_n)


if __name__ == "__main__":
    n = input()
    print solve(n)