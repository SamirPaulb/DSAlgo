# https://leetcode.com/problems/word-ladder-ii/

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        wordList = set(wordList) # making wordList a set so we can look-up a word in O(1) time
        if beginWord == endWord:
            return [beginWord] # if beginWord is the same as endWord we just return [beginWord] because there won´t be a shorter path
        q = collections.deque([[beginWord, []]])
        res = []
        while q:
            word, path = q.popleft() # word is the current word we´re on, path is the path that led us to this word
            if word in wordList:
                wordList.remove(word) # deleting the current word from wordList because we don´t want to go back
            if word == endWord:
                if not res or len(path) + 1 == len(res[0]): 
                    res.append(path + [word])
                elif len(path) + 1 > len(res[0]): # if the path that led us to this endWord is longer than the one in res, we know it´s longer and
                    break                         # all possible future paths will be longer so there´s no point in continuing
            else: # if the word isn´t endWord we find all words that differ by one character and continue in searching
                for i in range(len(word)):
                    for letter in alphabet:
                        next_word = word[:i] + letter + word[i+1:]
                        if next_word in wordList:
                            q.append([next_word, path + [word]])
        return res
