# https://practice.geeksforgeeks.org/problems/heap-sort/1


class Solution:
    
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        largest = i 
        l = 2 * i + 1  
        r = 2 * i + 2   
    
        #if left or right child is greater than current element, 
        #we store its position.
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
    
        #if largest is not equal to i, we swap the values at their position.     
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            #calling function recursively for the largest variable.
            self.heapify(arr, n, largest)
    
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        
        #calling heapify function for values from half to first index.
        for i in range(n, -1, -1):
            self.heapify(arr, n, i)
    
    #Function to sort an array using Heap Sort.
    def HeapSort(self,arr,n):
        
        #calling function to build heap with array.
        self.buildHeap(arr,n)
        
        for i in range(n - 1, 0, -1):
            
            #swapping values at current and first index.
            arr[i], arr[0] = arr[0], arr[i] 
            #calling heapify function for first index.
            self.heapify(arr, i, 0)
            
            
