def BinerySearch(l,key):
    low = 0
    high = len(l) - 1
    found = False
    while low<=high and not found:
        mid = (low + high)//2
        if key == l[mid]:
            found = True
        elif key < l[mid]:
            high = mid -1
        else:
            low = mid + 1
    if found == True:
        print("The value is found.")
    else:
        print("Value is not found!")
    
l = [2,3,4,6,64,24,453,33,4242,21]
l.sort()
print(l)
key = int(input("Enter the value of key:  ")) 
BinerySearch(l,key)
