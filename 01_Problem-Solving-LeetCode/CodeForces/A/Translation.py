__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/41/A
Solution: Base case checks if the lengths of the 2 strings does not equate. Otherwise, iterate
over either length and check from left and right of the 2 strings respectively for same character.
Return NO is it fails anywhere. Else, return YES after iteration.
'''
def solve(name1, name2):

    len1 = len(name1)
    len2 = len(name2)

    if(len1!=len2):
        return "NO"

    for i in range(0,len1):
        if(name1[i]!=name2[len1-i-1]):
            return "NO"

    return "YES"



if __name__ == "__main__":
    name1 = raw_input()
    name2 = raw_input()
    print solve(name1,name2)
