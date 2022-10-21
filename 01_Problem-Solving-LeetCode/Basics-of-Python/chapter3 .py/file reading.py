
#f = open('text.txt', 'r')
f = open('text.txt')   # by default the mode si r   that is read mode if it is a text file
data = f.read()
# data =  f.read(10)
print(data)
f.close()




