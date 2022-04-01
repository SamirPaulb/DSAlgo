# Heap in Python

Using Library functions :
We use heapq class to implement Heaps in Python. 
By default Min Heap is implemented by this class. 
But we multiply each value by -1 so that we can use it as MaxHeap.




### Max-Heap:
In a Max-Heap the key present at the root node must be greater than or equal among the keys present at all of its children. The same property must be recursively true for all sub-trees in that Binary Tree. In a Max-Heap the maximum key element present at the root. In pop operation root node is removed

```
import heapq
arr = [1, 3, 5, 34, 2, 9, 3534, 74]
for i in range(len(arr)):
    arr[i] *= -1

heapq.heapify(arr)

print( -1 * heapq.heappop(arr))  
# Output = 3534

```



### Min-Heap:
In a Min-Heap the key present at the root node must be less than or equal among the keys present at all of its children. The same property must be recursively true for all sub-trees in that Binary Tree. In a Min-Heap the minimum key element present at the root. In pop operation root node is removed

```
import heapq
arr = [1, 3, 5, 34, 2, 9, 3534, 74]
heapq.heapify(arr)

print(heapq.heappop(arr))  
# Output = 1  # as by default python heap is MinHeap
```