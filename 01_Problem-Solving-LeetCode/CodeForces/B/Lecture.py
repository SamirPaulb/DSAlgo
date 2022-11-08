__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/499/B

Solution: Keep a mapping of prof's words to student's words in a dictionary. Now run through the sentence and check 
if the mapped word (student's word) has a lesser length than the prof's word. If so, use it in the notes, else use profs.
This helps to give preference to prof's words when lengths are same. 
'''


def solve(dict, sentence):

    notesSentence = []

    for word in sentence:

        mappedWord = dict[word]

        if len(mappedWord) < len(word):
            notesSentence.append(mappedWord)
        else:
            notesSentence.append(word)

    return ' '.join(notesSentence)


if __name__ == "__main__":
    n,m = map(int, raw_input().split(" "))
    dict = {}
    for _m in xrange(0,m):
        words = raw_input().split(" ")
        dict[words[0]] = words[1]

    sentence = raw_input().split(" ")

    print solve(dict, sentence)