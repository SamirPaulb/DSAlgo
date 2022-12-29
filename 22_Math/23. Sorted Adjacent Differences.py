# https://codeforces.com/problemset/problem/1339/B

'''Solution: 
Sort the array. Keep 2 pointers left and right. Take the pair of elements of these pointed elements
in the result array. Move the left leftwards and right rightwards. This ensures the net distance on the 
number line is smallest, thereby agreeing to the constraint of absolute differences of pair elements.

For odd length arrays, we keep the middle element as the first element in the result array since it cannot
be paired. And then we start from the pointers movement as mentioned above.  
'''


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    res = [None] * n  

    if n % 2 == 0:
        left = n//2 - 1
        right = n//2
        i = 0
    else:
        left = n//2 - 1
        right = n//2 + 1
        res[0] = arr[n//2]
        i = 1
    
    while left >= 0 and right < n:
        res[i] = arr[left]
        left -= 1
        i += 1

        res[i] = arr[right]
        right += 1
        i += 1
    
    print(*res)
