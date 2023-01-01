'''
https://codeforces.com/problemset/problem/1294/C
 
Solution: We first find the factor for n using a standard sqrt time complexity stub. If we could 
find one, that becomes a. And then we find factor for n/a which is not equal to a. If we could
find one, that becomes b. By then, the value of n is made (n/a)/b or n/ab. Hence if that value of
n is not equal to a,b or 1 then it is c. We add it to the distinct factor's set and return the result.
At any step if we fail, the answer returned is NO. 
'''


def solve(n):

    distinct_factors = set()

    done, a = find_factors(n, distinct_factors)
    if not done:
        return "NO"
    else:
        n /= a

    done, b = find_factors(n, distinct_factors)
    if not done:
        return "NO"
    else:
        n /= b

    if n in distinct_factors or n == 1:
        return "NO"
    else:
        distinct_factors.add(n)

    return "YES" + "\n" + " ".join(str(int(i)) for i in distinct_factors)


'''
Helper to find distinct factor for the current value of n
Time Complexity: O(sqrt(n))
'''


def find_factors(n, distinct_factors):

    factor = 2
    f = 2
    done = False
    while f * f <= n and not done:

        if n % f == 0 and f not in distinct_factors:

            distinct_factors.add(f)
            factor = f
            done = True

        f += 1

    return done, factor





if __name__ == "__main__":

    t = int(input())

    results = list()
    for _ in range(0, t):
        n = int(input())
        results.append(solve(n))

    for result in results:
        print(result)
