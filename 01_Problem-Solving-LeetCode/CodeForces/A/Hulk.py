__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/705/A

Solution: The idea is to alternate between "I hate" and "I love" phrases. Ever alternation is connected with a " that ".
And the final string ends with " it". 
'''


def solve(n):

    odd_phrase = "I hate"
    even_phrase = "I love"
    connector = " that "
    finisher = " it"

    result = odd_phrase

    for i in xrange(2, n+1):

        result += connector

        if i % 2 == 0:
            result += even_phrase
        else:
            result += odd_phrase

    result += finisher

    return result


if __name__ == "__main__":

    n = int(raw_input())
    print solve(n)
