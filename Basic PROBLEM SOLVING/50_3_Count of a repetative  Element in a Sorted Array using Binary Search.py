def BS_first(ll,key):
    left = 0
    right = len(ll)-1
    while left<=right:
        mid = int((left+right)/2)
        if key == ll[mid]:
            a = mid
            right = mid - 1
        elif key > ll[mid]:
            left = mid +1
        else:
            right = mid -1
    return a

def BS_last(ll,key):
    left = 0
    right = len(ll)-1    
    while left<=right:
        mid = int((left+ right)/2)
        if key == ll[mid]:
            b = mid
            left = mid + 1
        elif key > ll[mid]:
            left = mid +1
        else:
            right = mid -1
    return b

key = int(input("Enter the repetative number from the list ll:  "))
ll = [1,2,4,5,6,7,7,7,7,7,7,7,7,7,7,7,464,6565,45467,4555555]

print(f"The number of repetation of {key} is =  {BS_last(ll,key)-BS_first(ll,key) +1}")


    
