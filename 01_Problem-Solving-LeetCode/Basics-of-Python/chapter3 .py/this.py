'''

with open('log.txt','r') as f:
    content = f.read()

with open("this.txt",'w') as f:
    f.write(content)

'''

file1 = "log.txt"
file2 = "this.txt"
with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2 = f.read()

if f1 == f2:
    print("Files are identical")
else:
    print("Files are NOT identical")


