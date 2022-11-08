__author__ = 'Devesh Bajpai'

'''
https://codeforces.com/problemset/problem/894/A

Solution: Observing the required string structure QAQ, we can deduce 2 important points:
1. For each A, we need to know how many Qs were present before it. That would help to create combination of QA with this
A
2. For each Q, we need to know how many QAQ and QA where present before it. The QAs of QAQs would combine with this Q to
build another QAQ. Also the earlier formed QAs would use this Q to form QAQ. 

Using this information, we can see that there is a sub-problem in this question which requires previous states of Q, QA
and QAQ to form their current counterparts. Hence solve this by using DP keeping the previous and current values of these
states. Finally, the answer lies in QAQ counter. Since we carry forward the current state value into its previous
one, in the end we will have the answer previous QAQ counter. 
'''


def solve(s):

    prev_q = curr_q = prev_qa = curr_qa = prev_qaq = curr_qaq = 0

    for i in xrange(0, len(s)):

        curr_q = curr_qa = curr_qaq = 0

        if s[i] == 'Q':
            curr_qaq = prev_qaq + prev_qa
            curr_q = prev_q + 1
        elif s[i] == 'A':
            curr_qa = prev_qa + prev_q

        prev_q = max(prev_q, curr_q)
        prev_qa = max(prev_qa, curr_qa)
        prev_qaq = max(prev_qaq, curr_qaq)

    return prev_qaq


if __name__ == "__main__":

    s = raw_input()
    print solve(s)
