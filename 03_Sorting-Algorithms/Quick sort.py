# Quick Sort Algorithm
# Learn theory from Abul Bari Sir (YouTube)

a = [10, 7, 8, 9, 1, 5]

def pivot_place(a, first, last):
    pivot = a[first]
    left = first + 1
    right = last
    while True:
        while left <= right and a[left] <= pivot:
            left += 1
        while left <= right and a[right] >= pivot:
            right -= 1
        if right < left:
            break
        else:
            a[left], a[right] = a[right], a[left]
    a[first], a[right] = a[right], a[first]
    return right

def quicksort(a, first, last):
    if first < last:
        p = pivot_place(a, first, last)
        quicksort(a, first, p-1)
        quicksort(a, p+1, last)


quicksort(a, 0, len(a)-1)
print(a)



