words = ['donkey','kaddu','bad','worst','mote']

with open('comment.txt','r') as f:
    a = f.read()

for word in words:
    a = a.replace(word,"@#$%@")
    with open('comment.txt','w') as f:
        f.write(a)
