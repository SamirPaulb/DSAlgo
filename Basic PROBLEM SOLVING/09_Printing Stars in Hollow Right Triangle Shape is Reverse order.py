'''
*********
 *      *
  *     *
   *    *
    *   *
     *  *
      * *
       **
        *

'''
n = int(input("type the number:   "))
print("*"*n)
for i in range(n,2,-1):
    print(" "*(n-i),"*"," "*(i-3),"*")
print(" "*(n-1),"*"*2)
print(" "*n,"*")






