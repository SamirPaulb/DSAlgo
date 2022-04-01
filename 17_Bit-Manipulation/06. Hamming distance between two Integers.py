# https://leetcode.com/problems/hamming-distance/
# https://www.geeksforgeeks.org/hamming-distance-between-two-integers/

'''
The Hamming distance between two integers is the number of positions
at which the corresponding bits are different.

Hamming distance between 4 (0100) and 14 (1110) is 2. as two bits at corresponding position are different
'''

def hammingDistance(n1, n2) :
 
    x = n1 ^ n2
    setBits = 0
 
    while (x > 0) :
        setBits += x & 1
        x >>= 1
     
    return setBits