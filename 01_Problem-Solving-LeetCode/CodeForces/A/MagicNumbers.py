__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/320/A

Solution: The question boils down to find the conditions to locate 1, 14 or 144. If 1 is observed, we go further
and check if 14 is present. If so, we go further and check if 144 is present. This way all the valid constituent
magic numbers are validated and the iterator is updated. If at the top level if check the value is not 1, it
is invalidating the rules and we return NO. 
'''


def solve(n):

    str_n = str(n)

    i = 0
    l = len(str_n)
    while i < l:

        # finding '1'
        if str_n[i] == '1':

            # finding '14'
            if i + 1 < l and str_n[i+1] == '4':

                # finding and is '144'
                if i + 2 < l and str_n[i+2] == '4':
                    i += 3
                # is '14'
                else:
                    i += 2

            # is '1'
            else:
                i += 1
        else:
            return "NO"

    return "YES"


if __name__ == "__main__":

    n = int(raw_input())
    print solve(n)
