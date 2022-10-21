import os
oldname = "siliguri.txt"
newname = "New_File.txt"
with open('siliguri.txt','r') as f:
    a = f.read()

with open('New_File.txt','w') as f:
    f.write(a)

os.remove(oldname)