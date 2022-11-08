__author__ = 'deveshbajpai'

'''
http://codeforces.com/problemset/problem/9/A
Algorithm: avlbl calculates the available possible dice values. Once that is available, the irr_fraction() computes the
irreducible fraction using the euclid algorithm based gcd computation. Results are printed as required.
'''

#euclid algorithm for gcd computation
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

def irr_fraction(num,dem):
    g = gcd(num,dem)
    while(g>1):
        num/=g
        dem/=g
        g = gcd(num,dem)

    print str(num)+"/"+str(dem)


def solve(y,w):

    avlbl = min(6,6-max(y,w)+1)
    irr_fraction(avlbl,6)


if __name__ == "__main__":
    y,w = map(int,raw_input().split(" "))
    solve(y,w)
