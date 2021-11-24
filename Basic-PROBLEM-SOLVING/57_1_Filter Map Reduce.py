nums = [1,2,4,5,34,67,4,8,64,48,90]

# To print even numbers from the list

def even(n):
    if n%2 ==0:
        return n

evens = list(filter(even, nums))

print(evens)
