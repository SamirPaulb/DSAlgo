__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/427/A

Solution: Run through the events. If its a crime, reduce the police available counter by 1 if we have any. Else this
crimes goes untreated and increase that counter. If the event is a recruitment, add the count to available police counter.
'''


def solve(events):

    untreatedCrimes = 0
    policeAvailable = 0

    for event in events:
        if event == -1:
            if policeAvailable > 0:
                policeAvailable -= 1
            else:
                untreatedCrimes += 1
        else:
            policeAvailable += event

    return untreatedCrimes


if __name__ == "__main__":

    n = int(raw_input())
    events = map(int, raw_input().split(" "))
    print solve(events)