__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1097/A

Solution: Brute force implementation to match each hand card's rank and suit with that of the one on the table.
If any of those match, return YES. Else NO.
'''


def solve(card_on_table, cards_in_hand):

    for card_in_hand in cards_in_hand:

        if card_in_hand[0] == card_on_table[0] or card_in_hand[1] == card_on_table[1]:
            return "YES"

    return "NO"


if __name__ == "__main__":

    card_on_table = raw_input()
    cards_in_hand = raw_input().split(" ")
    print solve(card_on_table, cards_in_hand)
