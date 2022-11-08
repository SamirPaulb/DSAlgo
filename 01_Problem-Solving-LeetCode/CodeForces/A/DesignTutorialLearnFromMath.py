__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/472/A

Solution: The idea is to explore even numbers as much as possible, since only 2 is a prime number.
Also, we'd like to keep at least one number in the pair static since we don't need to validate
both the numbers to be composite. We can split the cases as follows:

1. If n is even, we can try to split it into 2 even numbers > 2. The smallest value possible is
4. When n = 12, the other number is 8. Therefore we generalize 4, n - 4 as the pair. 

2. If n is odd, we can still try to get one number as even > 2. That is possible since odd -
even = odd. Now we need to make sure the other number which is odd, is not a prime since all primes
except 2 are odd. To ensure that safety, we make the odd number static. The smallest values possible 
is 9. When n = 13, the other number is 4. Therefore we generalize, 9, n - 9 as the pair. 
'''


def solve(n):

    if n % 2 == 0:
        result = [4, n - 4]
    else:
        result = [9, n - 9]

    return str(result[0]) + " " + str(result[1])


if __name__ == "__main__":

    n = int(raw_input())
    print solve(n)
