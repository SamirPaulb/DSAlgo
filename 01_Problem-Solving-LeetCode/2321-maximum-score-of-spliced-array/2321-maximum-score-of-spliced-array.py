class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        A = nums1
        B = nums2
        def kadane(A, B):
            cur, res = 0, 0
            for i in range(len(A)):
                cur += A[i] - B[i]
                res = max(res, cur)
                if cur < 0: cur = 0
            return res
        
        return max(sum(B) + kadane(A, B), sum(A) + kadane(B, A))
    