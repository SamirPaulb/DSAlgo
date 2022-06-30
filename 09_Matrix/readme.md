## The arr.copy() or arr[:] function of python works differently for 1D and 2D Arrays!

### For 1D Array:
```python
arr1 = [1, 2, 3]
arr2 = arr1.copy()  # or arr2 = arr1[:]

arr1[0] = 5   # this only changes value on arr1 NOT arr2

print(f"arr1 = {arr1}")   # [5, 2, 3]
print(f"arr2 = {arr2}")   # [1, 2, 3]
```

### For 2D Array:
```python
arr1 = [[1, 2], [3, 4]]
arr2 = arr1.copy()  # or arr2 = arr1[:]

arr1[0][0] = 5   # this changes value on both arr1 and arr2

print(f"arr1 = {arr1}")   # [[5, 2], [3, 4]]
print(f"arr2 = {arr2}")   # [[5, 2], [3, 4]]
```

> ***So to copy a 2D Array or Matrix we need to traverse the matrix and create new memory location for new Matrix*** 
 e.g. 
```python
arr1 = [[1, 2], [3, 4]]
arr2 = [[c for c in r] for r in arr1]
```
