'''
a = "           Samir Paul             "
print(a)
print(a.strip())


def remove_and_strip(string, word):
    newStr = string.replace(string,"")
    return newStr.strip()
this = "     Samir Paul is a good boy"
   
n = remove_and_strip(this,"Paul")
print(n)

'''