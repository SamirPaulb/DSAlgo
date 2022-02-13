# https://www.geeksforgeeks.org/consecutive-sequenced-numbers-in-a-string/
''' 
Given a string that contains only numeric digits, we need to check 
 whether that strings contains numbers in consecutive sequential manner
 in increasing order. 
Note: Negative numbers are not considered part of this problem.
 So we consider that input only contains positive integer.

Input :  str = "1234"
Output : Yes 
Explanation : 
There are 1, 2, 3, 4 which are 
consecutive and in increasing order.
And the starting number is 1

Input :  str = "91012"
Output : No
Explanation : 
There are no such sequence in the
string. 

Input :  str = "99100"
Output : Yes 
         99
Explanation : The consecutive sequential 
numbers are 99, 100

Input :  str = "010203"
Output : NO 
Explanation : 
Although at first glance there seems to
be 01, 02, 03. But those wouldn't be 
considered a number. 01 is not 1  it's 0, 1 
'''

string = "910911" 

n = len(string)
flag = False
for i in range(n//2):
    start = string[:i+1]
    num = int(start)
    tmp = ""
    while len(tmp) < n:
        tmp += str(num)
        num += 1
    if tmp == string: 
        flag = True
        break

print(flag)

