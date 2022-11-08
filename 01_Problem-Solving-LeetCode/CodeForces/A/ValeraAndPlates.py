__author__ = 'deveshbajpai'
'''
http://codeforces.com/problemset/problem/369/A
Algorithm: 2 major cases need to be considered. If 1st dish type are absent from his eating list, check if the difference
of 2nd dish and available bowls and plates is positive. If so, washing count is that difference.
In the second major case, individual 1st and 2nd dish types need to be considered when available utensils is less than
required. Add the differences for both dishes separately.

Status: This solution failed in 13th input. Check.
'''
class ValeraAndPlates:
    n = m = k = 0
    dishes = list()

    def solve(self):
        dish_m = self.dishes.count(1)
        #print dish_m
        dish_k = self.dishes.count(2)
        wash = 0

        if(dish_m==0 and dish_k>=(self.k+self.m)):
            wash+=dish_k-(self.k+self.m)
        else:
            if(self.m<dish_m):
                wash+=dish_m-self.m
            #print wash
            if(self.k<dish_k):
                wash+=dish_k-self.k
        print wash

if __name__ == "__main__":
    v = ValeraAndPlates()
    v.n,v.m,v.k = map(int,raw_input().split(" "))
    v.dishes = map(int,raw_input().split(" "))
    v.solve()