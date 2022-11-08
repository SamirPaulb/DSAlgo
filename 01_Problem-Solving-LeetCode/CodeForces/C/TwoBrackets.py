__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1452/C

Solution: Its easy to see that to form a RBS, we need to already have seen an opening bracket
before we see the closing bracket of the same kind. If that happens, we have a valid pair and
hence a RBS which can be eliminated. Therefore, we keep 2 counters to track the rounded and
squared brackets. Whenever their opening ones are seen, these counters are increased. On the
other side whenever their closing ones are seen, we check if the corresponding counter is 
positive and if so increase the total of RBS. Also we reduce the bracket counter denoting
the pair has been used i.e. removed.  
'''


def solve(bracket):

    round_bracket = square_bracket = total_rbs = 0

    for i in xrange(0, len(bracket)):

        if bracket[i] == '(':
            round_bracket += 1
        elif bracket[i] == '[':
            square_bracket += 1
        elif bracket[i] == ')':
            if round_bracket > 0:
                total_rbs += 1
                round_bracket -= 1
        elif bracket[i] == ']':
            if square_bracket > 0:
                total_rbs += 1
                square_bracket -= 1

    return total_rbs


if __name__ == "__main__":

    t = int(raw_input())

    for _ in xrange(0, t):
        bracket = raw_input()
        print solve(bracket)
