'''
https://codeforces.com/problemset/problem/1186/C
 
Solution: This question requires some effort to delve into and find a pattern. Lets take examples
of b and a's sub-array of equal length as a_arr and calculate f():

A)
b = 00110 and a_arr = 00111:

00110
00111

Ans: 1

B)
b = 00110 and a_arr = 01100:

00110
01100

Ans: 2

C)
b = 00010 and a_arr = 01110:

00010
01110

Ans: 2

D)
b = 00110 and a_arr = 00010:

00110
00010

Ans: 1

If you observe these examples, in cases where the count of 1s was same in b and a_arr, we ended up
having the answer even. This comes from the fact that same parity of count of 1s makes the resulting answer
to be always even. Odd +(or -) Odd is even and Even +(or -) Even is even. Therefore irrespective of 
which bits match, in such cases, the value of f() would always be even and that is what we
need to calculate in this question. 

Therefore, we calculate this observation in b and the first sub-array of a of length of b. Then
we slide the window of that length over a and compute it over subsequent sub-arrays of a. A counter
of same parity of these observations on b and a_arr is calculated and is the final answer. 

~ Tidbit ~
Checking parity between collections of bits is optimal via XOR operator rather than counting 
the occurrences and then using MODULO over 2. XOR alternates between 0 and 1 as we keep
operating it against 1, thereby denoting if the value is even or odd respectively. 

'''


def solve(a, b):

    len_a = len(a)
    len_b = len(b)

    bits_xored_subarr_a = 0
    bits_xored_b = 0

    # b and first sub-array of a
    for i in range(0, len_b):
        if a[i] == '1':
            bits_xored_subarr_a ^= 1
        if b[i] == '1':
            bits_xored_b ^= 1

    count = 0

    # inner sub-arrays of a
    for i in range(len_b, len_a):
        if bits_xored_subarr_a == bits_xored_b:
            count += 1
        if a[i] == '1':
            bits_xored_subarr_a ^= 1
        if a[i - len_b] == '1':
            bits_xored_subarr_a ^= 1

    # for the last sub-array of a
    if bits_xored_subarr_a == bits_xored_b:
        count += 1

    return count


if __name__ == "__main__":
    a = input()
    b = input()
    print(solve(a, b))
