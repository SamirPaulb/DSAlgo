__author__ = 'Devesh Bajpai'

'''
http://codeforces.com/problemset/problem/281/A
Nothing special. Just check the first character. If its in lowercase, print its upper case and
rest of the string as it is. Otherwise, print the original string as it is.
'''
if __name__ == "__main__":
    str = raw_input()

    if(len(str)>0 and str[0].islower()):
        print str[0].upper()+str[1:]
    else:
        print str
