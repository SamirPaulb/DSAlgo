'''
http://codeforces.com/problemset/problem/116/A
Solution: The idea is to simply calculate the net flow for the current station. Add it the current running
capacity. Compare it with the maximum recorded capacity; update it if current capacity exceeds it. 
'''
class Tram:
    def solve(self,n,stationStatus):
        maxCapacity = 0
        currCapcity = 0
        for currStatus in stationStatus:
            netFlow = currStatus[1]-currStatus[0]
            currCapcity+=netFlow
            if(currCapcity>maxCapacity):
                maxCapacity = currCapcity
        
        return maxCapacity
        
        
if __name__ == "__main__":
    stationStatus = list()
    n = int(raw_input())
    
    _n = 0
    while(_n<n):
        stationStatus.append(map(int,raw_input().split(" ")))
        _n+=1
    
    
    t = Tram()
    print t.solve(n,stationStatus)