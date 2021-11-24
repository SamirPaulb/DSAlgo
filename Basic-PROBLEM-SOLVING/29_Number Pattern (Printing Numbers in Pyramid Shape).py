'''
                              1  
                           2  1  2  
                        3  2  1  2  3  
                     4  3  2  1  2  3  4  
                  5  4  3  2  1  2  3  4  5  
               6  5  4  3  2  1  2  3  4  5  6  
            7  6  5  4  3  2  1  2  3  4  5  6  7  
         8  7  6  5  4  3  2  1  2  3  4  5  6  7  8  
      9  8  7  6  5  4  3  2  1  2  3  4  5  6  7  8  9  
   10 9  8  7  6  5  4  3  2  1  2  3  4  5  6  7  8  9  10 
11 10 9  8  7  6  5  4  3  2  1  2  3  4  5  6  7  8  9  10 11 
'''

n = int(input("Enter Number of rows:  "))

for row in range(1,n+1):
    for i in range(1,n-row+1):
        print(format(" ","<3"),end="")
    for j in range(row,0,-1):
        print(format(j,"<3"),end="")
    for k in range(2,row+1):
        print(format(k,"<3"),end="")
    print()

