def BinarySearch(l,key):
    low = 0
    high = len(l)-1
    found = False
    while low<=high and not found:
        mid = (low+high)//2
        if key == l[mid] :
            found = True
        elif key < l[mid]:
            high = mid -1
        elif key > l[mid]:
            low = mid +1
    if found ==True:
        print(f"The key {key} is found!")
    else:
        print(f"The key {key} is NOT found.")

l = [1,2,4,5,97,324,5464,5555555]
#key = int(input("enter a value within the list:  "))
BinarySearch(l,5)