'''
http://codeforces.com/problemset/problem/158/B
'''

from collections import defaultdict

class Taxi:
    def solve(self,n,students):
        #create frequency dictionary for students-count in list students
        d = defaultdict(int)
        for i in students:
            d[i] +=1
        
        taxiCount = 0
        
        
        #for all the 4student and 3student groups, we need separate taxis
        taxiCount+= d[4]+d[3]
        
        #for all 3student groups, we need to fill them with 1student groups
        d[1]-=d[3]
        #for all 2student groups, add their count to taxiCount
        taxiCount+= (d[2]/2)
        #for remaining 2student groups, one more taxi will be allocated
        if(d[2]%2>0):
            taxiCount+=1
            #deduct 2 1student groups to be adjusted in the 2student taxis 
            d[1]-=2
        #if any 1student groups are left 
        if(d[1]>0):
            taxiCount+=(d[1]/4)
            #for remaining 1student groups, one more taxi will be allocated
            if(d[1]%4>0):
                taxiCount+=1
        
        return taxiCount 
                
            
        
if __name__ == "__main__":
    students = list()
    n = int(raw_input())
    students = map(int,raw_input().split(" "))
    
    t = Taxi()
    print t.solve(n,students)