# https://practice.geeksforgeeks.org/problems/subarray-range-with-given-sum0128/1

import collections

class Solution:
    def subArraySum(self,arr, n, sum):
        s = res = 0
        cnt = collections.Counter()
        cnt[0] = 1
        for i in arr:
            s += i
            k = s-sum
            res += cnt[k]
            cnt[s] += 1
        return res
        
