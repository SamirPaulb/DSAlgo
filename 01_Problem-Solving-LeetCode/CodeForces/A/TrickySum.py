__author__ = 'bajde02'

'''
http://codeforces.com/contest/598/problem/A
Solution: Calculate the sum till num using AP sum formula. Now, remove all the powers of 2 from it and them as negated.
This can be done by starting a counter (say i) from 1 and going on till it reaches num. So, for 2^0, we already added
+1 in the sum. Now, since we have i==1, we get -2 which when removed from sum will firstly remove the earlier added
1 and add a -1 to it.
'''





def solve(num):
    sum=(num*(num+1))/2
    i=1
    while i<=num:
	    sum-=(2*i)
	    i*=2

    return sum

if __name__ == "__main__":

    cases = int(input())
    results = []
    for case in range(cases):
        results.append(solve(int(input())))

    for result in results:
        print result