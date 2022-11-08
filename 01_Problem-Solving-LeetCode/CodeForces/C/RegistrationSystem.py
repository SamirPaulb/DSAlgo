__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/4/C

Solution: Keep a map of names and the frequency of occurrence. For the first time, keep OK in the result, other wise
postfix the name with the frequency. Update the map in both cases. 
'''

def solve(n, names):

    db = {}
    result = []

    for i in xrange(0, n):

        if names[i] not in db:
            result.append("OK")
            db[names[i]] = 1
        else:
            postfix = db[names[i]]
            result.append(names[i] + str(postfix))
            db[names[i]] = postfix + 1

    return result



if __name__ == "__main__":

    n = int(raw_input())
    names = []
    for i in xrange(0, n):
        names.append(raw_input())

    result = solve(n, names)
    for i in xrange(0, n):
        print result[i]