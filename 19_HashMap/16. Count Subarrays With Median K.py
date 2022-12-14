# https://leetcode.com/problems/count-subarrays-with-median-k/
# https://youtu.be/QZzDioqkRhU

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pos = nums.index(k)
        cnt = defaultdict(int)
        cnt[0] = 1
        c = 0
        for i in range(pos + 1, len(nums)):
            c += 1 if nums[i] > k else -1
            cnt[c] += 1

        ans = cnt[0] + cnt[1]
        c = 0
        for i in range(pos - 1, -1, -1):
            c += 1 if nums[i] < k else -1
            ans += cnt[c] + cnt[c + 1]
        # print(cnt)
        return ans
