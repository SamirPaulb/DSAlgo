'''
with open('log.txt','r') as f:
    a = f.read().lower()

if 'python' in a:
    print("python is presnt")
else:
    print("python is NOT present")


'''

with open('log.txt','r') as f:
    a = f.read().lower()

if 'python' in a.lower():
    print("python is presnt")
else:
    print("python is NOT present")



