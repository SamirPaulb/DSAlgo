#  Check Given Two Strings Are Anagram or Not
#  HEART and EARTH  are Anagram
# abc  and   bca  are Anagram

a,b = input("").split(' ') 

if sorted(a) == sorted(b):
    print(f"Given  strings {a} and {b} are Anagram.")
else:
    print(f"Given  strings {a} and {b} are NOT Anagram.")



