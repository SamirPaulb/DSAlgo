__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/222/A
Solution: The array is becoming same by replicating the kth element at the end of the array
Now, we first check if the elements after the kth to n contains any element which is not same
as kth element, then the array cannot be made same as required . Return -1.
Else, start checking from k-1 to 0 index and find the first index which does not matches
with the kth element. This is the number of moves required to make the array same.
'''
class ShooshunandSequence:
    n = 0
    k = 0
    seq = list()

    def solve(self):

        #find if elem at kth index is present in array from k+1 to n
        for i in range(self.k,self.n):
            if(self.seq[i]!=self.seq[self.k-1]):
                return -1

        #find the nearest index of different value from the kth index
        i_req = 0
        for i in range(self.k-2,-1,-1):
            if(self.seq[i]!=self.seq[self.k-1]):
                #print "val ",self.seq[i]
                i_req = i+1
                break

        return i_req

if __name__ == "__main__":
    s = ShooshunandSequence()
    s.n,s.k = map(int,raw_input().split(" "))
    s.seq = map(int,raw_input().split(" "))

    print s.solve()