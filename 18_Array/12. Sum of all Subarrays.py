# https://www.geeksforgeeks.org/sum-of-all-subarrays/


'''
Given an integer array ‘arr[]’ of size N, find the sum of all sub-arrays of the given array. 

Input: arr[] = {1, 2, 3}
Output: 20
Explanation: {1} + {2} + {3} + {2 + 3} + {1 + 2} + {1 + 2 + 3} = 20

Input: arr[] = {1, 2, 3, 4}
Output: 50
'''



def SubArraySum(arr, n):
    result = 0
 
    # computing sum of subarray
    # using formula
    for i in range(0, n):
        result += (arr[i] * (i+1) * (n-i))
 
    # return all subarray sum
    return result
 
 
# Driver code
arr = [1, 2, 3]
n = len(arr)
print("Sum of SubArray : ",
      SubArraySum(arr, n))
