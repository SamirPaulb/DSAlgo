## list.pop(0) vs deque.popleft()

q = collections.deque()

pop(0) removes the first item from the list and it requires to 
shift left len(lst) - 1 items to fill the gap.

deque() implementation uses a doubly linked list. No matter how large the deque, deque. popleft() requires a constant (limited above) number of operations.

The time complexity of deque.popleft() is O(1), while the time complexity of list.pop(0) is O(k), 
as index 0 is considered an intermediate index.