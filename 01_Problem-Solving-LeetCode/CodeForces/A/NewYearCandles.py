__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/379/A

Solution: a candles would burn for a hours. After that, we have a burnt candles, and we can take sets of b candles and
build one candle. In other words, we can build a/b candles from it. And we keep progressing. It may feel that we need
to update the candles to burn (a) by a/b since that is that we would be left in every iteration. But we ignore the 
remainder candles (a%b). In iterations, we may have those remainders that can add up and make another candle which
can be burnt as well. 

Let's see an example. a = 123, b = 5

hours = 0

1) The 123 candles burn for an hour. So we start with hours = a = 123.

2) After 123 hours, we build 123/5 = 24.6 candles formed by using the half-burnt candles. So hours = 123 + 24 = 147.
a = 123/5 + 123%5 = 24 + 3 = 27

3) After 24 hours, we build 27/5 = 5.4 candles formed by using half-burnt candles. So hours = 147 + 5 = 152. 
a = 27/5 + 27%5 = 5 + 2 = 7

4) After 7 hours, we build 7/5 = 1.4 candles formed by using half-burnt candles. So hours = 152 + 1 = 153.
a = 7/5 + 7%5 = 1 + 2 = 3

Now since the remaining candles is lesser than b = 5, we will never be able to build a new candle and hence the work stops.
Hence the iteration has a condition that a >= b which means we should have at least b no. of candles left to burn.

Now you can understand if we had ignored the a%b in updating a, we would record 151 as the final answer. 

'''


def solve(a, b):

    hours = a

    while a >= b:
        hours += (a/b)
        a = (a / b) + (a % b)

    return hours


if __name__ == "__main__":
    a, b = map(int, raw_input().split(" "))
    print solve(a, b)
