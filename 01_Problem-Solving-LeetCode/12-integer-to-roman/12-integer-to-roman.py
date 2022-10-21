class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        dic =  {1000:"M",
                900 :"CM",
                500 :"D" ,
                400 :"CD",
                100 :"C" ,
                90  :"XC",
                50  :"L" ,
                40  :"XL",
                10  :"X" ,
                9   :"IX",
                5   :"V" ,
                4   :"IV",
                1   :"I" 
                }
        
        for i in dic:
            res += dic[i] * (num // i)
            num = num % i
        
        return res
    
# Time Complexity: O(1);  as it is constant independent on num
# Space Complexity: O(1); constant space