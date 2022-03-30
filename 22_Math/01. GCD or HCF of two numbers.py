# https://www.geeksforgeeks.org/c-program-find-gcd-hcf-two-numbers/
'''
GCD (Greatest Common Divisor) or HCF (Highest Common Factor)
of two numbers is the largest number that divides both of them. 
'''
# Euclidean Algorithm: GCD of two numbers doesn’t change if smaller number is subtracted from a bigger number. 
# https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/

# --------------------------------------------------------------------------------------------------

# Recursive function to return gcd of a and b
def gcd(a,b):
     
    # Everything divides 0
    if (a == 0):
        return b
    if (b == 0):
        return a
    # base case
    if (a == b):
        return a
 
    # a is greater
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)

# Time Complexity: O(max(a,b))
# Auxiliary Space: O(max(a,b))

# ------------------------------------------------------------------------------------------------


# Dynamic Programming Approach (Top Down Using Memoization)
# Taking the matrix as globally
dp = [[-1 for i in range(1001)] for j in range(1001)]
 
def gcd(a,b):
     
    # Everything divides 0
    if (a == 0):
        return b
    if (b == 0):
        return a
 
    # base case
    if (a == b):
        return a
     
    if(dp[a][b] != -1):
        return dp[a][b]
         
    # a is greater
    if (a > b):
        dp[a][b] = gcd(a-b, b)
    else:
        dp[a][b] = gcd(a, b-a)
         
    return dp[a][b]

# Time Complexity: O(max(a,b))
# Auxiliary Space: O(1)

# ------------------------------------------------------------------------------------------------


# Use Modulo Operator in Euclidean Algorithm
def gcd(a,b):
     
    # Everything divides 0
    if (b == 0):
         return a
    return gcd(b, a%b)

# Time Complexity: O(log(max(a,b))
# Auxiliary Space: O(log(max(a,b))