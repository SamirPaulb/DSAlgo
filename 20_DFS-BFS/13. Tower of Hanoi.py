# https://practice.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1
# https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/

class Solution:
    def toh(self, n, from_rod, to_rod, aux_rod):
        if n == 0: 
            return 0
        moves = 1
        moves += self.toh(n-1, from_rod, aux_rod, to_rod)
        print("move disk", n, "from rod", from_rod, "to rod", to_rod)
        moves += self.toh(n-1, aux_rod, to_rod, from_rod)
        return moves
