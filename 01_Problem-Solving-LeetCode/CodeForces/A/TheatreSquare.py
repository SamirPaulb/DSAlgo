'''
https://codeforces.com/problemset/problem/1/A

Theatre Square in the capital city of Berland has a rectangular shape with the size n × m meters. On the occasion of the city's anniversary, a decision was taken to pave the Square with square granite flagstones. Each flagstone is of the size a × a.

What is the least number of flagstones needed to pave the Square? It's allowed to cover the surface larger than the Theatre Square, but the Square has to be covered. It's not allowed to break the flagstones. The sides of flagstones should be parallel to the sides of the Square.

Input
The input contains three positive integer numbers in the first line: n,  m and a (1 ≤  n, m, a ≤ 109).

Output
Write the needed number of flagstones.
'''
class TheatreSquare:
    
    def solve(self,n,m,a):
        
        return ((n-1)/a+1)*((m-1)/a+1)
        


if __name__ == "__main__":
    
    n,m,a = map(int,raw_input().split(" "))
    ts = TheatreSquare()
    
    print ts.solve(n,m,a)
    
    