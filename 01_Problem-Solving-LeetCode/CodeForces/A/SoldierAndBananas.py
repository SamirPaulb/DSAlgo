'''
https://codeforces.com/problemset/problem/546/A

Solution: Using the AP formula, the total money needed is (1+2+..w)*k
That simplifies to ((w*(w+1)) * k)/2. This is the sum of first w natural numbers, multiplied by k
Then take the difference of that with soldier's initial money, which is n. If he does not need money, we need to set 0.
Hence we use max to compare the the difference against 0.
'''

def solve(k, n, w):

    totalMoneyNeeded = ((w*(w+1)) * k)/2
    return max(totalMoneyNeeded - n, 0)


if __name__ == "__main__":
    inputs = raw_input().split(" ")
    print solve(int(inputs[0]), int(inputs[1]), int(inputs[2]))