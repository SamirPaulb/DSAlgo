# https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1
# https://www.youtube.com/watch?v=2JSQIhPcHQg

''' 
A = [12,34,67,90];  M = 2

I will implement Binary Search with left pointer l and right pointer r.
As I know max(A) must be given to a student so l = max(A); you can start from l = 0 also
l = max(A) = 90
r = sum(A) = 203

90----------------------------------------------------------------146--------------------------------------------203
l                                                                 mid                                             r
mid = 146 isValid so ans = mid = 146; I will try to decrease mid => r = mid - 1 = 145 

90-------------------------------------117------------------------145
l                                      mid                         r
mid = 117 isValid so ans = mid = 117; I will try to decrease mid => r = mid - 1 = 116

90--------------103--------------------116
l               mid                     r
mid = 103 NOT isValid so I will try to increase mid => l = mid + 1 = 104

                104-------110----------116
                 l        mid           r
mid = 110 NOT isValid so I will try to increase mid => l = mid + 1 = 111

                          111----113---116
                           l     mid    r
mid = 113 isValid so ans = mid = 113; I will try to decrease mid => r = mid - 1 = 112

                          111----112
                          l=mid   r
mid = 111 NOT isValid so I will try to increase mid => l = mid + 1 = 112

                                 112
                                l=mid=r
mid = 112 NOT isValid so I will try to increase mid => l = mid + 1 = 113
Now l = 113; r = 112    => l > r   => Break Loop 

'''

class Solution:
    def findPages(self,A, N, M):
        l = max(A); r = sum(A); ans = -1
        
        if len(A) < M: return -1  # Number of books can not be lesser than number of students as we have to give atleast 1 book to a student

        def isValid(A, M, mid):
            pageSum = 0           # sum of pages of A that can be allocated to one student
            requiredStudents = 1  # Number of students required if mid is the max capacity of student
            
            for pages in A:
                pageSum += pages
                if pageSum > mid:          # sum of pages allocated to one student exceed max capacity of the student
                    requiredStudents += 1  # We need one more student
                    pageSum = pages        # start calculating sum of pages that can be allocated to next student
            
            if requiredStudents > M: return False
            else: return True
        
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if isValid(A, M, mid):
                ans = mid         # Updating answer to current mid as current mid is the most optimized(least) ans till now
                r = mid - 1       # I will try to decrease mid
            else:
                l = mid + 1       # current mid NOT isValid so I will try to increase mid
        
        
        return ans                # Most Optimized ans is stored here
        
        