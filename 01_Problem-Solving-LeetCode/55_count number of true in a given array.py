
def CountTrue(a):
    num = 0
    for i in range(len(a)):
        if a[i].lower() == "true":
            num =  num +1 
    return num
    

a = ["True", "false", "true", "true", "false", "false"]
print(CountTrue(a))



