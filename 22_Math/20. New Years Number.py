'''
https://codeforces.com/problemset/problem/1475/B
B. New Year's Number
'''
 

t  = int(input())

for _ in range(t):
      n = int(input())
      if n < 2020:
            print('NO')
      else:
            if n % 2020 <= n / 2020:
                  print('YES')
            else:
                  print('NO')
