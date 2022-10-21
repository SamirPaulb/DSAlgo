a = "Hello World!"
def reverse(a):
    s = ""
    for i in a:
        s = i + s
    return s

print(reverse(a))
