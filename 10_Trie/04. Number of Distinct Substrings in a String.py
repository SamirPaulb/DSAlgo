# https://www.codingninjas.com/codestudio/problems/count-distinct-substrings_985292
# https://youtu.be/RV0QeTyHZxo
class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def solve(self, s):
        res = 0
        for i in range(len(s)):
            cur = self.root
            for j in range(i, len(s)):
                if s[j] not in cur.children:
                    cur.children[s[j]] = TrieNode()
                    res += 1
                cur = cur.children[s[j]]
        return res + 1  # +1 for empty substring ""

def countDistinctSubstrings(s):
    trie = Trie()
    return trie.solve(s)


# Time: O(N^2)
# Space: It is hard to predict spcace taken tries. It depends on the distinct elements of s. But as we are using only necessary keys in trie hashmap not all 26 keys so at max space can be N^2
# Space: in worst case O(N^2)
    