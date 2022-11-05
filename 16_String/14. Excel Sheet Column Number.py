# https://leetcode.com/problems/excel-sheet-column-number/

'''
  A.....to......Z = 26 elements
  AA.....to......ZZ = 26*26 elements
  AAA...to.....ZZZ = 26^3 elements
  so on.....
  
  therefore for eg :  ABCD

  ABCD = [(A)*26^3] + [(B)*26^2] + [(C)*26^1] + [(D)] 
  
  where (A) = 1,(B) = 2 ......(AA) = 27....
  
  eg : "ZY" --->
--first Y , ord(Y) = 89,-->89-64=25(value of Y in the first 26 elements),therefore its excel sheet value will be = [(26^0)*25] == 25
--second Z, ord(Z) = 90,-->90-64=26(value of Z in the first 26 elements) ,therefore its excel sheet value will be = [(26^1)*26] == 656
taking summ of them gives "ZY"'s column number i.e, 656 + 25 = 701

'''


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        p = 1
        ans = 0
        
        for ch in columnTitle[::-1]:
            ans += p * (ord(ch) - 64)
            p *= 26
        
        return ans


    
