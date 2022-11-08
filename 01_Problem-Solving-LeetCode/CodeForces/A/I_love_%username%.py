__author__ = 'deveshbajpai'
'''
Problem Url: http://codeforces.com/problemset/problem/155/A

Algorithm: For the input scores, maintain the smallest and the largest score encountered so far. Run a loop over the
scores and update either if pass the conditions, and also capture them as amazing events i.e. increase the amazing
counter. The final value of this counter at end of the loop is the answer.
'''


def solve(scores):
    smallest = largest = scores[0]
    amazing = 0
    for score in scores[1:]:
        if(score < smallest):
            smallest = score
            amazing+=1
        if(score > largest):
            largest = score
            amazing+=1
    return amazing

if __name__ == "__main__":

    n = int(input())
    scores = map(int,raw_input().split(" "))
    print solve(scores)