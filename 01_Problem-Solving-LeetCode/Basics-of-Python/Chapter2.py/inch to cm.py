'''
n =10
def countup(n):
    if n >= 0:
        countup(n - 1)
        print(n)

'''

n = int(input("Type a number in inch here: "))
def cem(n):
    return n*2.54
print(cem(n))

