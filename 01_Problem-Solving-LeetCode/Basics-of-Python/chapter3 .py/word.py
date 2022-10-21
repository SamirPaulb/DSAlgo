'''

with open('poem.txt','r') as f:
    a = f.read()
if "twinkle" in a :
    print("Twinkle is present")
else: 
    print("Twinkle is NOT present")
    

    '''

f = open('poem.txt')
a = f.read()
if "twinkle" in a :
    print("Twinkle is present")
else: 
    print("Twinkle is NOT present")
    
