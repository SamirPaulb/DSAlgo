__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/977/B

Solution: The idea is to take all the two-grams in the string and maintain the frequency map of them. In the end, just
query the frequency map to return the key (two-gram string) which has the highest value (its frequency).

'''


def solve(n, str):

    twoGramMap = {}

    for i in xrange(0, n):

        currTwoGram = str[i:i+2:]

        if len(currTwoGram) < 2:
            break

        freq = twoGramMap.get(currTwoGram, 0) #getOrDefault() equivalent
        twoGramMap[currTwoGram] = freq+1

    maxOccurTwoGram = max(twoGramMap, key=lambda freq: twoGramMap[freq])
    return maxOccurTwoGram


if __name__ == "__main__":
    n = int(raw_input())
    str = raw_input()
    print solve(n, str)
