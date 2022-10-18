# https://practice.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1

#Tower of Hanoi
class Solution:
    def toh(self, N, fromm, to, aux):
        if(N == 1):
            print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
            return 1
        # recursive call to move top disk from "from" to aux in current call
        moves = 0
        moves += self.toh(N - 1, fromm, aux, to)
        moves += 1 # increment moves
        print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
        #recursive call to move top disk from aux to "to" in current call
        moves += self.toh(N - 1, aux, to, fromm)
        return moves
