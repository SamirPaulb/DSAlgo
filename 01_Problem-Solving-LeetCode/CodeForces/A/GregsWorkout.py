__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/255/A

Solution: Get the sum of the exercise counts for the 3 types. The quicker pythonic way is to use the following notation
to get sub-list : listVar[startIndex:endIndex:step].
Using this, we need every third exercise count, starting from 0 for chest, from 1 for biceps and 2 for back.
Interestingly this takes care if the list doesn't have enough elements to get that sub-list. Find the sums and return
the max-one. 

'''


def solve(exercises):

    chest = sum(exercises[0::3])
    biceps = sum(exercises[1::3])
    back = sum(exercises[2::3])

    maxExercise = "chest"

    if biceps > chest and biceps > back:
        maxExercise = "biceps"
    elif back > chest and back > biceps:
        maxExercise = "back"

    return maxExercise



if __name__ == "__main__":
    n = int(raw_input())
    exercises = map(int, raw_input().split(" "))

    print solve(exercises)