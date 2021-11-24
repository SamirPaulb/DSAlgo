'''

Calculate time required to type a word using given single-row keyboard

    Last Updated : 12 Mar, 2021

Given a string keyboardLayout of size 26 representing the sequence of characters present in a single row of a keyboard and a string word, the task is to calculate the total time taken to type the word, starting from the 0th key, if moving to adjacent keys requires unit time.

Examples:

    Input: keyboardLayout = “abcdefghijklmnopqrstuvwxyz”, word = “dog”
    Output: 22
    Explanation:
    Pressing the key ‘d’ requires 3 units of time ( i.e. ‘a’ -> ‘b’ -> ‘c’ -> ‘d’)
    Pressing the key ‘o’ requires 11 units of time ( i.e. ‘d’ -> ‘e’ -> ‘f’ -> ‘g’ -> ‘h’ -> ‘i’ -> ‘j’ -> ‘k’ -> ‘l’ -> ‘m’ -> ‘n’ -> ‘o’)
    Pressing the key ‘g’ requires 8 units of time ( i.e. ‘o’ -> ‘n’ -> ‘m’ -> ‘l’ -> ‘k’ -> ‘j’ -> ‘i’ -> ‘h’ -> ‘g’)
    Therefore, the total time taken = 3 + 11 + 8 = 22.

    Input: keyboardLayout = “abcdefghijklmnopqrstuvwxyz”, word = “abcdefghijklmnopqrstuvwxyz”
    Output: 35

'''


A =  "abcdefghijklmnopqrstuvwxyz"
S = "dodiefjg"
sum = 0
previous = 0
for i in range(len(S)):
    current = A.index(S[i])
    if current >= previous:
        sum += current - previous
    else:
        sum += previous - current

    previous = current

print(sum)



