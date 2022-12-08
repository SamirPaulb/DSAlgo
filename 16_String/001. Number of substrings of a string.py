# https://www.geeksforgeeks.org/number-substrings-string/


# Python3 program to count number
# of substrings of a string
 
def countNonEmptySubstr(str):
    n = len(str)
    return int(n * (n + 1) / 2)
 
s = "abcde"
print (countNonEmptySubstr(s))
