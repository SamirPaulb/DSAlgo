__author__ = 'deveshbajpai'
'''
Problem Url: http://codeforces.com/problemset/problem/527/A

Algorithm: Make dictionary with key as pre-contest rating and value as post-contest rating. Since students with same
pre-contest rating will have same post-contest rating, this dictionary is helpful as it keeps distinct keys only.
Now sort the students list, but maintain the original list for printing in the end. The rating of the first student
in the sorted list is 1. Start the iteration after that. If the current student is same as previous, then just copy
latter's rating to former in the dictionary. Else, use the formula of current index plus 1. This calculates to total
number of student above him + 1. In the end, iterate over the original list of students and print their corresponding
post-contest rating from the dictionary.
'''


def solve(students,count):
    #this map has key as student pre-contest rating and value as post-contest rating
    students_ratings = dict()
    for student in students:
        students_ratings[student] = 0

    #make a copy for sorted list of students
    #original list is maintained to print the result in order of original input
    sorted_students = sorted(students,reverse=True)

    #first student in the sorted list get 1st rating
    students_ratings[sorted_students[0]] = 1

    for i in xrange(1,count):
        student = sorted_students[i]
        prev_student = sorted_students[i-1]
        if student == prev_student:
            students_ratings[student] = students_ratings[prev_student]
        else:
            students_ratings[student] = 1 + i


    #print the ratings
    for student in students:
        print students_ratings[student],

if __name__ == "__main__":
    count = int(input())
    students = map(int,raw_input().split(" "))
    solve(students,count)