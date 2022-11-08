'''
http://codeforces.com/problemset/problem/131/A
Solution: each case is explained in comments.

'''
class cAPSlOCK:
    def solve(self,str):
        #if blank string is input, return is unformatted
        if(len(str)==0):
            return str
        #if single lowercase in input, convert to uppercase and return
        if(len(str)==1 and str.islower()):
            return str.upper()
        
        #if the complete string is uppercase, conver the whole string to lower case and return
        if(str.isupper()):
            return str.lower()
        
        #if the first character is lowercase and remain substring is uppercase, 
        #convert the reverse of both parts and return
        if(str[0].islower() and str[1:].isupper()):
            return str[0].upper()+str[1:].lower() 
        
        return str
        
        
if __name__ == "__main__":
    str = raw_input()
    c = cAPSlOCK()
    print c.solve(str)
