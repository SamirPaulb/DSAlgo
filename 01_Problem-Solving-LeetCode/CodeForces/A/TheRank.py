__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1017/A

Solution: The idea is to transform the list of scores in list of tuples where each value has the original id and the
sum of scores. Then we sort this new list of tuples using a custom comparator. It sorts in decreasing order of scores 
and break ties using increasing order of ids. Post this sorting, we traverse it and find the position of the id 0. That
is the rank. +1 is added to convert it into a 1-indexed rank. 
'''


def solve(n, scores):

    scores_ids = list()
    for id in xrange(0, n):
        scores_ids.append([id, sum(scores[id])])

    scores_ids.sort(cmp=custom_comparator)

    for id in xrange(0, n):

        if scores_ids[id][0] == 0:
            return id + 1 # rank is required in 1-indexed value

    return -1


# sort by scores in decreasing order, and break ties using ids in increasing order
def custom_comparator(score_id1, score_id2):

    if score_id1[1] == score_id2[1]: # same scores
        return score_id1[0] - score_id2[0] # increasing order of ids
    else: # different scores
        return score_id2[1] - score_id1[1] # decreasing order of scores


if __name__ == "__main__":

    n = int(raw_input())

    scores = list()
    for _ in xrange(0, n):
        score = map(int, raw_input().split(" "))
        scores.append(score)
    print solve(n, scores)
