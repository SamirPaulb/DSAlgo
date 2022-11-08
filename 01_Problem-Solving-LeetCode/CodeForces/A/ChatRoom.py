__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/58/A
Algorithm: Iterate over the string and maintain the index for word hello. If they match for the complete word hello,
return YES. Else NO.
'''

def solve(str):
    word = "hello"
    index = 0
    for i in range(0,len(str)):
        if(index==5):
            return "YES"
        if(str[i]==word[index]):
            index+=1

    if(index<5):
        return "NO"
    else:
        return "YES"



if __name__ == "__main__":
    str = raw_input()
    print solve(str)
