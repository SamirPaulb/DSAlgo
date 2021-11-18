def BinarySearch(l,key ):
    low = 0
    high = len(l)-1
    while low <= high:
        mid = int((low+high)/2)
        if l[mid] ==key:
            res = mid
            low = mid+1
        elif key < l[mid]:
            high = mid-1
        else:
            low = mid+1
    print(f"Last Occurence of {key} is = {res}")
        



l = [1,2,4,5,97,97,97,64,97,97,324,5464,5555555]
#key = int(input("enter a value within the list:  "))
BinarySearch(l,97)
