class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[-1] += 1
        if digits[-1] == 10:
            carry = 1
            digits[-1] = 0
            
        for i in range(len(digits)-2, -1, -1):
            digits[i] += carry
            if digits[i] == 10:
                carry = 1
                digits[i] = 0
            else:
                carry = 0
        
        return digits if carry == 0 else [carry] + digits