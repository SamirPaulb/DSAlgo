# https://codeforces.com/problemset/problem/1355/B

t = int(input())
for _ in range(t):
      n = int(input())
      arr = list(map(int, input().split()))
      
      arr.sort()
      cur_size = 0
      total_size = 0
      for i in arr:
            cur_size += 1
            if cur_size == i:
                  total_size += 1
                  cur_size = 0

      print(total_size)
