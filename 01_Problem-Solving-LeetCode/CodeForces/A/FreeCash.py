__author__ = 'deveshbajpai'

'''
http://codeforces.com/problemset/problem/237/A

Algorithm: Maintain a dictionary of input times with their frequency as their values. Once all the inputs are taken,
run over the dictionary and find the frequency which is maximum of all. That is the number of cashes needed.
'''



if __name__ == "__main__":

    n = int(input())

    inputs = {}

    for _n in xrange(n):
        time = raw_input()
        if(time in inputs):
            inputs[time]+=1
        else:
            inputs[time]=1

    cash = 0
    for time in inputs:
        if(inputs[time]>cash):
            cash = inputs[time]
    print cash
