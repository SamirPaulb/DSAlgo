def BinarySearch(l,key):
    low = 0
    high = len(l)-1
    mid = 0

    while low<=high:
        mid = (low+high)//2
        if key == l[mid] :
            res = mid
            high = mid-1
        elif key < l[mid]:
            high = mid -1
        elif key > l[mid]:
            low = mid +1
    print("mid=",res)
    
        
l = [1,2,4,5,97,97,97,97,97,324,5464,5555555]
#key = int(input("enter a value within the list:  "))
BinarySearch(l,97)