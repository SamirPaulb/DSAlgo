__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/59/A
Solution: Count the number of upper case letters.
Check for length of string to be odd or even and accordingly check if the string
of upper case or not. If so, convert the string to upper case. Else, convert to lowercase.
'''

word = raw_input()
l = len(word)
#check if the word has majority upper case letters or not
count = 0
for i in range(0,l):
    if(word[i]>='A' and word[i]<='Z'):
        count+=1

#make cases for both even and odd length
if((l%2==0 and count>(l/2)) or (l%2==1 and count>=(l/2)+1)):
    print word.upper()
else:
    print word.lower()
