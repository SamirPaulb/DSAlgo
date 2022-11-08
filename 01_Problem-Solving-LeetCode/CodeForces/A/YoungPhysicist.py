__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/69/A
Solution: Brute force solution. Run through the vectors and calculate the sum of
x,y and z components. In the end, if all components are 0, return YES; else NO.
'''
def solve(vectors):
    x_count = y_count = z_count = 0

    for vector in vectors:
        x_count += vector[0]
        y_count += vector[1]
        z_count += vector[2]


    if(x_count==y_count==z_count==0):
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":

    cases = int(input())
    vectors = []
    for x in range(cases):
        vector = map(int,raw_input().split(" "))
        vectors.append(vector)
    print solve(vectors)