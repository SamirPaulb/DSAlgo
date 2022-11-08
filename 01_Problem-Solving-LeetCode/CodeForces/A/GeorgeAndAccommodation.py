__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/467/A

Solution: Just need to check for each room, the difference of max occupancy (q) and current occupancy (p) is >= 2
or not. If so, the room can accommodate George and Alex and hence increase the counter.  
'''


def solve(all_room_values):

    count = 0

    for room_values in all_room_values:

        if room_values[1] - room_values[0] >= 2:
            count += 1

    return count


if __name__ == "__main__":

    n = int(raw_input())

    all_room_values = list()
    for _ in xrange(0, n):
        room_values = map(int, raw_input().split(" "))
        all_room_values.append(room_values)

    print solve(all_room_values)
