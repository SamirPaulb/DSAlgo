# https://www.spoj.com/problems/EKO/

n = int(str[0])
M = int(str[1])

arr = map(int, input().split())

def isValid(arr, M, mid):
    amount = 0
    for height in arr:
        if height > mid:
            amount += height - mid
    return amount >= M

low = 0
high = max(arr)

while low <= high:
    mid = low + (high - low) // 2
    if isValid(arr, M, mid):
        low = mid + 1
    else:
        high = mid - 1

print(low)


# Time: O(n * log(max(arr)))
# Space: O(1)




def chopped_off(heights, t):
    return sum(max(i-t, 0) for i in heights)


def search_optimal_height(heights, threshold):
    lo = min(heights) - threshold
    hi = max(heights)
    while lo <= hi:
        mid = (hi + lo)//2
        if chopped_off(heights, mid) >= threshold:
            lo = mid+1
        else:
            hi = mid - 1
    return hi


n, m = map(int, raw_input().split())
heights = [int(i) for i in raw_input().split()]
ans = search_optimal_height(heights, m)
print(ans)