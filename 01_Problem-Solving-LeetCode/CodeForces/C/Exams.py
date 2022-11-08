__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/479/C

Solution: Sort the exam dates by their actual dates since those are the ones which will be recorded. Now use a variable
to capture the last exam's date (initialized to the first exam's early date) and iterate over the list of exam dates.
For every exam, if the last exam's date is lesser than the early date of current exam, set former to later. If not, 
set the former to actual exam's date.  

~ Tidbit ~
Use cmp argument in sort() to pass a custom comparator function. 
'''

# Sort by actual exam dates but if they are same, sort by their early exam dates
def customCompare(exam_date1, exam_date2):

    if exam_date1[0] == exam_date2[0]:
        return exam_date1[1] - exam_date2[1]
    else:
        return exam_date1[0] - exam_date2[0]


def solve(exam_dates):

    # sort by actual date of exams
    exam_dates.sort(cmp=customCompare)

    last_exam_date = exam_dates[0][1]

    for i in xrange(1, len(exam_dates)):

        actual_date = exam_dates[i][0]
        early_date = exam_dates[i][1]

        if early_date >= last_exam_date:
            last_exam_date = early_date
        else:
            last_exam_date = actual_date

    return last_exam_date


if __name__ == "__main__":

    t = int(raw_input())

    exam_dates = list()
    for _ in xrange(0, t):
        a, b = map(int, raw_input().split(" "))
        exam_dates.append([a, b])

    print solve(exam_dates)
