__author__ = 'Devesh'
'''
http://codeforces.com/problemset/problem/112/A
Solution: Run a loop over any string's length (since they are said to have same length)
Convert each letter of both string to same case and compare. Return -1 and 1 accordingly.
If complete strings match, 0 is returned.
'''


def compare(str1, str2):

    for i in range(0,len(str1)):
        if(str1.lower()[i]<str2.lower()[i]):
            return -1
        elif(str1.lower()[i]>str2.lower()[i]):
            return 1
    return 0
if __name__ == "__main__":
    str1 = raw_input()
    str2 = raw_input()

    print compare(str1,str2)

