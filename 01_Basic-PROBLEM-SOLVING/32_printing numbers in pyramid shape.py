'''
                  1     
               2     3     
            4     5     6     
         7     8     9     10    
      11    12    13    14    15    
   16    17    18    19    20    21    
22    23    24    25    26    27    28    
'''

row = int(input("Enter the number of rows:   "))
n = 1
for i in range(row):
    for j in range(row-i-1):
        print(format(" ","<3"),end="")
    for k in range(i+1):
        print(format(n,"<6"),end="")
        n = n+1
    print()



    

    
