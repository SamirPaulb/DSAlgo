__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/959/B

Solution: The question is simple but the implementation is the key. We construct a dictionary
of words to their minimum cost. That is obtained by going over the groups and querying the
group member's index in the costs array to pull their cost, and calculate the minimum per group.
This key - value is updated in a dictionary. Now we go over the words in the message and sum
the words' minimum cost from this dictionary. This is the final answer. 
'''


def solve(words, costs, groups, msg):

    word_to_min_cost = {}

    for group in groups:

        this_group_cost = 1000000000 # upper limit as mentioned in the question
        for i in group:
            this_group_cost = min(this_group_cost, costs[i-1]) #i-1 since group indices are 1 - indexed

        for i in group:
            word_to_min_cost[words[i-1]] = this_group_cost #i-1 since group indices are 1 - indexed

    msg_cost = 0
    for word in msg:
        msg_cost += word_to_min_cost[word]

    return msg_cost


if __name__ == "__main__":

    n, k, m = map(int, raw_input().split(" "))
    words = raw_input().split(" ")
    costs = map(int, raw_input().split(" "))
    groups = list()
    for _ in xrange(0, k):
        group = map(int, raw_input().split(" "))
        groups.append(group[1:]) #exclude the first element which is the length of the group
    msg = raw_input().split(" ")

    print solve(words, costs, groups, msg)
