__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/1287/A

Solution: Since the only students that are turned angry for patient need to be after the angry student, we need to count
those int he given sequence. The longest length of those initially patient students would be the total time taken to 
make the last possible student angry. We keep counter (post_angry_patient_count) for this length, reset it whenever an 
angry student is detected, and keep a maximum of all values of this counter (max_post_angry_patient_count). 
'''


def solve(n, students):

    angry_idx = -1
    post_angry_patient_count = 0
    max_post_angry_patient_count = 0

    for i in xrange(0, n):

        if students[i] == 'A':
            angry_idx = i
            post_angry_patient_count = 0
        elif angry_idx != -1:
            post_angry_patient_count += 1

        max_post_angry_patient_count = max(post_angry_patient_count, max_post_angry_patient_count)

    return max_post_angry_patient_count


if __name__ == "__main__":

    t = int(raw_input())

    for _ in xrange(0, t):
        n = int(raw_input())
        students = raw_input()
        print solve(n, students)
