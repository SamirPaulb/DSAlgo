__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1367/C

Solution: The algorithm is to find blocks of k 0s and then put a customer at the start of that block. For doing that,
we keep an inner loop to check the block of k tables. If we find anyone occupied, we start the iteration from its next
table, else we place a new customer on the start of the block (ie. increase the counter of new customer).
'''


def solve(n, k, s):

    i = new_customer_count = 0
    while i < n:

        if s[i] == '0':

            is_block_of_k_tables_occupied = False
            for j in xrange(i+1, min(i+k+1, n)):

                if s[j] == '1':
                    i = j
                    is_block_of_k_tables_occupied = True
                    break

            if not is_block_of_k_tables_occupied:
                new_customer_count += 1
                i += k+1
        else:
            i += k+1

    return new_customer_count


if __name__ == "__main__":

    #t = 1
    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):

        #n = 2
        #k = 1
        #s = "01"
        n, k = map(int, raw_input().split(" "))
        s = raw_input()

        results.append(solve(n, k, s))

    for result in results:
        print result
