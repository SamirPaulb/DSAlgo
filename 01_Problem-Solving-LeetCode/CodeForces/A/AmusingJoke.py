__author__ = 'Devesh Bajpai'
'''
http://codeforces.com/problemset/problem/141/A
Solution: Create frequency distribution (lexically ordered) of each word. Add them to make
their joint distribution. Compare with the similar distribution of the jumbled words.
If they match, return YES. Else return NO.
'''
class AmusingJoke:
    name1 = ""
    name2 = ""
    jumbLetters = ""

    def solve(self):
        from collections import Counter, OrderedDict

        map1 = Counter(self.name1)
        map2 = Counter(self.name2)
        map_jumLtr = OrderedDict(Counter(self.jumbLetters))
        if (OrderedDict(map1+map2)==map_jumLtr):
            return "YES"
        else:
            return "NO"


if __name__ == "__main__":
    a = AmusingJoke()
    a.name1 = raw_input()
    a.name2 = raw_input()
    a.jumbLetters = raw_input()
    print a.solve()