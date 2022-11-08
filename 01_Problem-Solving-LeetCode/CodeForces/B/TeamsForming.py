__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1092/B

Solution: Firstly, we sort the skills list. That makes the adjacently placed students (or more correctly their skills)
most apt to be paired in a team, as their skill level would be the nearest in comparison to all the rest of students.
Now we run a loop through this sorted skill list in a step of 2, and add the difference of current student with his
right neighbor. Since its sorted in ascending order, its safe to subtract the right student's skill with that of left's. 
This total sum is the minimum skills needed to form teams.  
'''


def solve(n, skills):

    skills.sort()

    total_skills_needed = 0
    for i in xrange(0, n, 2):

        total_skills_needed += (skills[i+1] - skills[i])

    return total_skills_needed


if __name__ == "__main__":
    n = int(raw_input())
    skills = map(int, raw_input().split(" "))
    print solve(n, skills)
