# https://leetcode.com/problems/maximum-xor-with-an-element-from-array/

# First SOLVE: 03. Maximum XOR of Two Numbers in an Array (https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0
    
class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def addNum(self, num):
        cur = self.root
        for i in range(31, -1, -1):
            bit = 1 if num & (1 << i) else 0
            if bit not in cur.children:
                cur.children[bit] = TrieNode()
            cur = cur.children[bit]
        cur.val = num
        
    def getMax(self, x):
        cur = self.root
        maxi = 0
        for i in range(31, -1, -1):
            bit = 1 if x & (1 << i) else 0  
            if bit == 1:
                if 0 in cur.children:
                    cur = cur.children[0]
                elif 1 not in cur.children: 
                    return -1
                else:
                    cur = cur.children[1]
            else: # bit = 0
                if 1 in cur.children:
                    cur = cur.children[1]
                elif 0 not in cur.children: 
                    return -1
                else:
                    cur = cur.children[0]
        maxi = cur.val ^ x
        # print(maxi)
        return maxi
        
    def maximizeXor(self, nums, queries):
        nums.sort()
        res = [-1] * (len(queries))
        
        for i in range(len(queries)):
            queries[i].append(i)
        
        queries.sort(key = lambda x:x[1])
        
        n = 0; q = 0
        while q < len(queries):
            while n < len(nums) and nums[n] <= queries[q][1]:
                self.addNum(nums[n])
                n += 1
            res[queries[q][2]] = self.getMax(queries[q][0])
            q += 1
        
        return res
