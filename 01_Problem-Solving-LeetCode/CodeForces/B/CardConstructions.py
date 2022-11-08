__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1345/B

Solution: Quite a mathematical question. 
The first requirement is form a formula that relate the total number of cards to the maximum height pyramid possible,
if only one pyramid was to be made from it. 

--------------------------------------
Case A: Height = 1, cards needed = 2

Shape: /\


--------------------------------------
Case B: Height = 2, cards needed = 7

Shape: 

 /\
  _
/\ /\

--------------------------------------
Case C: Height = 2, cards needed = 15

Shape: 

  /\
   _
 /\ /\
  _  _
/\ /\ /\

--------------------------------------

Now let's deduce the formula. If we observe, there is structure of inverted V in all pyramids. Lets take the count of
those in each case as V.

So we have, 
Case A: Height = 1, V = 1
Case B: Height = 2, V = 1 + 2
Case C: Height = 3, V = 1 + 2 + 3

Hence, basically its the AP sum of numbers from 1 to h (height). But since every inverted V has 2 cards, we can deduce:

Case A: Height = 1, n' = 2*1
Case B: Height = 2, n' = 2*(1 + 2)
Case C: Height = 3, n' = 2*(1 + 2 + 3)
...
Case h: Height = h, n' = 2*(1+2+...h) = 2*( (h*(h+1))/2 ) = h*(h+1)

Now we handle the flat lying cards in each case, and can deduce its formula as:
Case A: Height = 1, n" = 0
Case B: Height = 2, n" = 1
Case C: Height = 3, n" = 1 + 2
...
Case h: Height = h, n" = 1+2+...h-1 = (h*(h-1))/2  

Hence total of those two formula would be:

h*(h+1) + (h*(h-1))/2  =  (3h^2 + h)/2 

Now this should be equal to the given number of cards, say n. This forms the quadratic equation: (3h^2 + h)/2 = n
It can be solved for its roots (using shridhar acharya formula) which comes as:

(-1/2 + sqrt(1/4 + 6*n))/3. Note we ignored the -ve solution as we want to solve for positive height of pyramids. 
Therefore, we can use it solve for the highest pyramid height that is possible for the given number of cards. Then, we
can use that height, rounded to the floored integer to get its actual number of cards needed. This can be deducted from
the total card count. We keep repeating this process till we have valid number of cards to build the smallest pyramid, 
which is 2 (of height 1). 
 


'''
import math

def solve(card_counts):

    pyramids_possible = list()
    for card_count in card_counts:
        #print card_count

        total_pyramids = 0
        while card_count >= 2:

            highest_pyramid_height = (math.sqrt((6 * card_count) + 0.25) - 0.5)/3

            highest_pyramid_cards_needed = cards_needed_for_given_height(int(highest_pyramid_height))

            if card_count >= highest_pyramid_cards_needed:
                card_count -= highest_pyramid_cards_needed
            else:
                break

            total_pyramids += 1

        pyramids_possible.append(total_pyramids)

    return "\n".join(str(p) for p in pyramids_possible)


def cards_needed_for_given_height(h):
    return (h * ((3*h) + 1))/2


if __name__ == "__main__":
    t = int(raw_input())
    card_counts = list()
    for _t in xrange(0,t):
        card_counts.append(int(raw_input()))
    print solve(card_counts)

