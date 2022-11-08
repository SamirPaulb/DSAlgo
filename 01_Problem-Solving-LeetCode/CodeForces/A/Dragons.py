__author__ = 'deveshbajpai'

'''
https://codeforces.com/problemset/problem/230/A

TODO: Not all testcases are passing
'''

def pairSort(inputs):

    for i in xrange(0,len(inputs)):
        for j in xrange(1,len(inputs)):
            if(
                    (inputs[i][0]>inputs[j][0])
                or (inputs[i][0]==inputs[j][0] and inputs[i][1]<inputs[j][1])

            ):
                print 'cond',inputs[i][0],inputs[i][1]
                x_temp = inputs[i][0]
                y_temp = inputs[i][1]
                inputs[i][0] = inputs[j][0]
                inputs[i][1] = inputs[j][1]
                inputs[j][0] = x_temp
                inputs[j][1] = y_temp

def solve(inputs,s):
    pairSort(inputs)
    print inputs
    for i in xrange(0,len(inputs)):
        if(s>inputs[i][0]):
            s=s+inputs[i][1]
        else:
            return "NO"
    return "YES"


if __name__ == "__main__":

    s,n = map(int,raw_input().split(" "))
    x = []
    y = []
    inputs = []
    for _n in xrange(n):
        x_val,y_val =  map(int,raw_input().split(" "))
        inputs.append([x_val,y_val])

    #print inputs
    print solve(inputs,s)
