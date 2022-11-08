__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/401/A
Solution: Sum all the numbers available in the cards list. If the current sum is more than
0, try to make it zero. For that, check if the current sum - x is becoming >= 0. If so,
subtract it and reiterate. Else, reduce x by 1. Keep doing this till the sum becomes 0.
Now for the case when the initial sum was negative, do the reverse of the above step.
Keep counting the missing cards whenever the sum is updated. Return missing as the answer.
'''
class VanyaandCards:

    n = -1
    x = -1
    cards = list()

    def solve(self):
        sum = 0
        for card in self.cards:
            sum += card
        #print sum

        missing = 0
        if(sum>0):
            while(sum>0):
                if(sum-self.x >= 0):
                    sum-= self.x
                    missing +=1
                else:
                    self.x -= 1
        elif(sum<0):
            while(sum<0):
                if(sum+self.x <= 0):
                    sum+= self.x
                    missing +=1
                else:
                    self.x -= 1

        return missing


if __name__ == "__main__":
    v = VanyaandCards()
    v.n,v.x = map(int, raw_input().split(" "))
    v.cards = map(int, raw_input().split(" "))
    print v.solve()