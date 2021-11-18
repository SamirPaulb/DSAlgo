'''Note:
list_initial = [2,5,6,8,11,12,15,18]
after rotation,
list_rotated =  [11,12,15,18,2,5,6,8]
Note:
index of Minimum element = Number of times the array is rotated

in list_rotated index of 2 is 4 which is equal to 4 times the array is rotated

again to determine the minimum element---->> previous and next element of the minimum element should be greater
than the minimum element  here in list_rotated, 2<5 and 2<18
 And to determine the minimum element we have to search in the unsorted array
'''

def BS(l,n):
    start = 0
    n = len(l)
    end = n-1
    while start <=end:
        mid = int((start+end)/2)
        next = (mid+1)%n
        prev = (mid+n-1)%n
        if l[mid] <= l[next] and l[mid] <= l[prev]:
            a = mid
        elif l[end] <= l[mid]:
            start =  mid
        elif l[start] >= l[mid]:
            end = mid
    return a

# here a is index of Minimum element = Number of times the array is rotated

l = [11,12,15,18,2,5,6,8]

print(f"Number of Times a Sorted array is Rotated =  {BS(l,8)}")


