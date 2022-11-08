'''
http://codeforces.com/problemset/problem/96/A

Solution: Make a regex of 7 consecutive 1s and another of 7 consecutive 0s. If they match, return YES, else NO.
Base case condition is to check if length of given string is less than 7. Return NO in this case.

'''
class Football:
    def solve(self,footballers):
        if(len(footballers)<7):
            return "NO"
        
        import re
        match_ones = re.search(r'\d*1111111\d*',footballers)
        match_zeroes = re.search(r'\d*0000000\d*',footballers)
        
        if(match_ones or match_zeroes):
            return "YES"
        else:
            return "NO"
       
        
        
if __name__ == "__main__":
    footballers = raw_input()
    f = Football()
    print f.solve(footballers)