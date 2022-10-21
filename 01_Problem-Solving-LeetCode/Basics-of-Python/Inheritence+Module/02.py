'''
from dir import myfunction
print(myfunction.add(3,5))
print(myfunction.multiply(10,40))
'''


'''
import dir.myfunction
print(dir.myfunction.add(3,5))
print(dir.myfunction.multiply(10,40))
'''


import dir.myfunction as mf
print(mf.add(5,8))
print(mf.multiply(5,8))

