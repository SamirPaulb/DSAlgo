'''
       * 
      * * 
     * * * 
    * * * * 
   * * * * * 
  * * * * * * 
 * * * * * * * 
'''
n = int(input("enter no. of rows: "))
i = 1
while i <=n:
    j = n-i
    while j>=0:
        print(end=" ")
        j = j-1
    print("* "*i)
    i = i+1

