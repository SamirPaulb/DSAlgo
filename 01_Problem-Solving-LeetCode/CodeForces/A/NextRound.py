'''
https://codeforces.com/problemset/problem/158/A

"Contestant who earns a score equal to or greater than the k-th place finisher's score will advance to the next round, as long as the contestant earns a positive score..." - an excerpt from contest rules.

A total of n participants took part in the contest (n>=k), and you already know their scores. 
Calculate how many participants will advance to the next round


Input
The first line of the input contains two integers n and k separated by a single space.

The second line is the non-increasing score list
Output
Output the number of participants who advance to the next round.

'''
class NextRound:
    def solve(self,n,k,numList):
        result = 0
        for i in numList:
            if(i>0 and i>=numList[k-1]):
                result+=1
        return result
        
        
        

if __name__ == "__main__":
    
    numList = list()
    n,k = map(int,raw_input().split(" "))
    numList = map(int,raw_input().split(" "))
    nr = NextRound()
    print nr.solve(n,k,numList)