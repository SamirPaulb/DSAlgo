# https://leetcode.com/problems/design-an-atm-machine/

class ATM:

    def __init__(self):
        self.dollers = [20, 50, 100, 200, 500]
        self.count = [0, 0, 0, 0, 0]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.count[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        countCopy = self.count.copy()  # making a copy to handel not valid cases([-1])
        res = [0, 0, 0, 0, 0]
        for i in range(4, -1, -1):
            res[i] = min(amount // self.dollers[i], countCopy[i])
            countCopy[i] -= res[i]
            amount -= self.dollers[i] * res[i]
        
        if amount != 0: return [-1]   # for this case count updated in copy version not the real self.count
        self.count = countCopy  # for this valid case decrease the count 
        return res
            
            

# Time: O(N)
# Space: O(N)