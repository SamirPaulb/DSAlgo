# YouTube Video: https://www.youtube.com/watch?v=mqaf7vj1AdA&list=PL5tcWHG-UPH1kjiE-Fqt1xCSkcwyfn2Jb
"""
Bisect:
    -"Built-in" binary search method in Python.
    -Can be used to search for an element in a sorted list.
""" 

# Import allows us to make use of the bisect module.
import bisect

# This sorted list will be used throughout this video
# to showcase the functionality of the "bisect" method.
A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

# The bisect_left function finds index of the target element.
# In the event where there are duplicate entries satisfying the target
# element, the bisect_left function returns the left-most occurrence.

# -10 is at index 1
print(bisect.bisect_left(A, -10))

# First occurrence of 285 is at index 6
print(bisect.bisect_left(A, 285))

# The bisect_right function returns the insertion point which comes after,
# or to the right of, any existing entries in the list.

# Index position to right of -10 is 2.
print(bisect.bisect_right(A, -10)) 

# Index position after last occurrence of 285 is 9.
print(bisect.bisect_right(A, 285))

# There is also just a regular default "bisect" function. This function
# is equivalent to "bisect_right":

# Index position to right of -10 is 2. (Same as bisect_right)
print(bisect.bisect(A, -10)) 

# Index position after last occurrence of 285 is 9. (Same as bisect_right).
print(bisect.bisect(A, 285))

# Given that the list A is sorted, it is possible to insert elements into
# A such that the list remains sorted. Functions "insort_left" and 
# "insort_right" behave in a similar way to "bisect_left" and "bisect_right",
# only the insort functions insert at the index positions.
print(A)
bisect.insort_left(A, 108)
print(A)

bisect.insort_right(A, 108)
print(A)