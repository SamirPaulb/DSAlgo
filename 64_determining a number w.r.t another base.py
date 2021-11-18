class Solution:
    def sumBase(self, n: int, k: int) -> int:
        sum = 0
        if n >= 1 and n<= 100 and k>= 2 and k<= 10:
            while n != 0:
                sum = sum + n%k
                a = n//k
                n = a
            return sum

base_num = Solution()

n = int(input(""))
k = int(input(""))

print(base_num.sumBase(n,k))