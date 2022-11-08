__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1294/B

Solution: At the sight of this question, it may appear that we need to perform DFS while maintaining the different paths 
and finally returning the lexicographically smallest one. But we don't need to actually simulate the DFS. 

Since the robot can move only Right and Up, it cannot go from co-ordinate x1, y1 to x2, y2 if either x1 < x2 and y1 > y2,
or x1 > x2 and y1 < y2. This is because to do this movement, the robot would need to move Left or Down which isn't in
its skills. Hence we sort the co-ordinates and check if we find any such adjacent co-ordinates. 

In order to find the path, we can calculate the Right and Up distance and append that many Rs and Us to the path string. 
In order to choose the lexicographically smallest one, we make sure that we prefer Right over Up since R < U 
lexicographically. We also perform initial sorting of the packages w.r.t. to x co-ordinates first and then y 
co-ordinates. This makes sure that when we're processing them for the movement, we always get them in the order that 
gives the lexicographically smallest path string. 
'''


def solve(n, packages):

    packages.sort(cmp=compare)

    path = []
    curr = (0, 0)

    for i in xrange(0, n):

        package = packages[i]

        if (package[0] > curr[0] and package[1] < curr[1]) or (package[0] < curr[0] and package[1] > curr[1]):
            return "NO"

        right_distance = package[0] - curr[0]
        up_distance = package[1] - curr[1]

        for _ in xrange(0, right_distance):
            path.append("R")
        for _ in xrange(0, up_distance):
            path.append("U")

        curr = package

    return "YES" + "\n" + "".join(_ for _ in path)


def compare(package1, package2):
    if package1[0] != package2[0]:
        return package1[0] - package2[0]
    else:
        return package1[1] - package2[1]


if __name__ == "__main__":

    t = int(raw_input())

    results = list()
    for _ in xrange(0, t):
        n = int(raw_input())
        packages = list()
        for __ in xrange(0, n):
            package = map(int, raw_input().split(" "))
            packages.append(package)
        results.append(solve(n, packages))

    for result in results:
        print result
