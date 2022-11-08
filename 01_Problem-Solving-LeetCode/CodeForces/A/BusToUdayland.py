'''
https://codeforces.com/problemset/problem/711/A

Solution: Straightforward. Use the brute force technique to go through the bus rows and check if we get free seats
together on either left or right side of tha aisle. Occupy them and break the loop. Print the modified bus allocation
is the decision is YES.

'''

free = "OO"
book = "++"
aisle = "|"
bus = []

def solve(n):

    ans = "NO"
    for i in xrange(0,n):
        sides = bus[i].split(aisle)

        #left side of aisle
        if sides[0] == free:
            bus[i] = book + aisle + sides[1]
            ans = "YES"
            break
        #right side of aisle
        elif sides[1] == free:
            bus[i] = sides[0] + aisle + book
            ans = "YES"
            break

    return ans


if __name__ == "__main__":
    n = int(raw_input())
    for i in xrange(0,n):
        bus.append(raw_input())

    ans = solve(n)

    print ans

    if ans == "YES":
        for i in xrange(0,n):
            print bus[i]