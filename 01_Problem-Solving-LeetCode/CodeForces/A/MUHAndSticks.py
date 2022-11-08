__author__ = 'deveshbajpai'
'''
Problem Url: http://codeforces.com/problemset/problem/471/A

Algorithm: Since we have 6 sticks and for being a bear or elephant, we need to have legit 4 legs of equal lengths.
Therefore are are only 3 possibilities of the legs to occur in a sorted list of sticks:

0 L L L L 0
L L L L 0 0
0 0 L L L L

Hence we can track the starting index of the legs. Based on that we can get the index of other 2 sticks (non-legs)
On those 2 sticks we can decide if they are equal or not and return Elephant or Bear respectively.

If the legs are not found at all, or belong to some other format, we do not have 4 legit legs. Hence return Alien.
'''


def solve(legs):

    legs.sort()


    leg_starting_index = -1
    for i in xrange(0,len(legs)-3):
        if legs[i] == legs[i+1] == legs[i+2] == legs[i+3]:
            leg_starting_index = i
            break


    #3 possibilities if leg_starting_index is found
    if leg_starting_index == 1:
        return bear_or_elephant_decider(legs,0,5)
    elif leg_starting_index == 2:
        return bear_or_elephant_decider(legs,0,1)
    elif leg_starting_index == 0:
        return bear_or_elephant_decider(legs,4,5)
    else:
        return "Alien"



def bear_or_elephant_decider(legs, index1, index2):
    if legs[index1] != legs[index2]:
        return "Bear"
    else:
        return "Elephant"



if __name__ == "__main__":
    legs = map(int,raw_input().split(" "))
    print solve(legs)