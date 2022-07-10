## Binary Search

We should write **mid = start + (end - start)//2**
because in some test cases mid = (start + end)//2 may give ***Integer Overflow Error***

or,

**mid = (low + high) >> 1**   
right shift by 1 bit 
