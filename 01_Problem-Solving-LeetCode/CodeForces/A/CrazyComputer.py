__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/716/A

Solution: Keep a running count of the words on the screen. If the ith word has been typed after c seconds of the i-1th
word, the screen is cleared and hence we reset the running count of words on screen to 0. Then we add 1 to the count
for the ith word. Finally, the value of count is the number of words that persisted on the screen.  
'''


def solve(n, c, typeTimestamps):

    wordsOnScreen = 1 #consider the first word already typed and available on the screen
    for i in xrange(1, n):

        if typeTimestamps[i] - typeTimestamps[i-1] > c:
            wordsOnScreen = 0 #screen is cleared
        wordsOnScreen += 1 #the ith word is added to the screen

    return wordsOnScreen


if __name__ == "__main__":

    n, c = map(int, raw_input().split(" "))
    typeTimestamps = map(int, raw_input().split(" "))
    print solve(n, c, typeTimestamps)
