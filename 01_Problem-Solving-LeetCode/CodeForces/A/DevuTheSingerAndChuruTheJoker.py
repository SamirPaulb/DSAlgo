__author__ = 'deveshbajpai'
'''
Problem Url: http://codeforces.com/problemset/problem/439/A

Algorithm: We can infer that since each pair of songs have to have 2 jokes in between (10 mins = 2 Charu's jokes),
minimum number of required jokes = 2(n-1). The actual possible jokes can be done in the remaining duration after the
songs, which is d - songs_total. Now, we have a minimum no of jokes and actual possible jokes count. If latter is
greater than or equal to that former, we return the jokes possible count. Otherwise, return -1.
'''


def solve(n,d,songs):

    minimum_jokes_required = 2*(n-1)

    songs_total = 0

    for song in songs:
        songs_total += song

    jokes_possible = (d - songs_total)/5

    if jokes_possible >= minimum_jokes_required:
        return jokes_possible
    else:
        return -1

if __name__ == "__main__":
    n,d = map(int,raw_input().split(" "))
    songs = map(int,raw_input().split(" "))
    print solve(n,d,songs)