__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1355/B

Solution: If the question was finding minimum number of groups, we'd just create 1 and put all the people in it. 
Since we need to find maximum, we need a strategy where we fill a group with just enough people. That means we need to 
track the people in an ordering of their inexperience value. Hence we first sort the inexperience list in ascending 
order. Now as we traverse it, we keep track of the size of current group. Ideally we'd want to stop filling it as soon
as we have enough people in it. To find that, we check if the current person's inexperience is equal to the size of the
group. That means it would satisfy the constraint with this person and all the remaining people in that group. 
So we add this group to the total and reset the current group size. There is a chance we might not get to fill the group
while the inexperience list exhausts, in that case we don't consider this group. 

Let's work through an input inexperience list:
Given:   2, 3, 1, 2, 2
Sorted:  1, 2, 2, 2, 3

Traversing:
Initially, current_group_size = 0, total_groups = 0

First Person:
current_group_size = 1, total_groups = 0, exp = 1
This person goes in the current group. Size their exp matches the group size, we have enough strength in it.
So, current_group_size = 0, total_groups = 1 

Second Person:
current_group_size = 1, total_groups = 1, exp = 2

Third Person:
current_group_size = 2, total_groups = 1, exp = 2
Again, we have enough in the current group so we move on to next group.
So, current_group_size = 0, total_groups = 2

Fourth Person:
current_group_size = 1, total_groups = 2, exp = 2

Fifth Person:
current_group_size = 2, total_groups = 2, exp = 3
And we exhaust the list. Note that this current group (3rd one) that we were building didn't get enough people in it. 
So the members of this group would've joined the other 2 groups we already built.

Hence, in total we just had 2 groups. 

'''


def solve(n, exp_list):

    exp_list.sort()
    curr_group_size = total_groups = 0

    for exp in exp_list:

        curr_group_size += 1
        if curr_group_size == exp:
            total_groups += 1
            curr_group_size = 0

    return total_groups


if __name__ == "__main__":
    test_cases = int(raw_input())
    results = list()
    for testcase in xrange(0, test_cases):
        n = int(raw_input())
        exp_list = map(int, raw_input().split(" "))
        results.append(solve(n, exp_list))
    for result in results:
        print result
