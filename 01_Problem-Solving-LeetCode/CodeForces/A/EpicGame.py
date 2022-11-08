__author__ = 'Devesh'
'''
http://codeforces.com/problemset/problem/119/A
Solution: Implement turns for each player using a turn variable and checking its value to be
odd or even. GCD is implemented using recursive euclid algorithm. Rest all is pretty straight-
forward.
'''

#GCD using euclid algorithm
def gcd(a,b):
    if(b == 0):
	    return a
    return gcd(b, a%b)

def solve(a,b,n):
    turn = 0
    while(True):
        if(turn%2==0):
            #print "Simon turn"
            toPick = gcd(a,n)
            if(n>=toPick):
                n-=toPick
            else:
                return 1 #consider win for Antisimon
        else:
            #print "Antisimon turn"
            toPick = gcd(b,n)
            if(n>=toPick):
                n-=toPick
            else:
                return 0 #consider win for Simon
        turn+=1


if __name__ == "__main__":
    inputs = raw_input()
    a = int(inputs.split(" ")[0])
    b = int(inputs.split(" ")[1])
    n = int(inputs.split(" ")[2])

    print solve(a,b,n)