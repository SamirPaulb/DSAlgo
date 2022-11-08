'''
https://codeforces.com/problemset/problem/492/A

Solution:

Say n = 25.

Per layer Boxes   | Total Boxes Used
1                 |      1
1+2 = 3           |      4
1+2+3 = 6         |     10
1+2+3+4 = 10      |     20
1+2+3+4+5 = 15    |     35

Hence at each layer, we add the height (incremented by 1 in each layer) to the previous-layer boxes and that
gives the current layer boxes. Keep adding that to a total accumulation (boxesUsed).

Since we cannot build a layer without having enough boxes for the current-layer, we may over-estimate the height.
Hence, we check if n < boxesUsed after the current layer usage, we reduce the height by 1, thereby descarding the
current layer in the pyramid.

The final height is the answer.

'''

def solve(n):

    height = boxesUsed = prevStepBoxes = 0

    while n > boxesUsed:

        height += 1
        thisStepBoxes = prevStepBoxes + height
        boxesUsed += thisStepBoxes
        prevStepBoxes = thisStepBoxes

        #if this layer is not possible, we over-estimated the height. Reduce it by 1
        if n < boxesUsed:
            height -= 1

    return height


if __name__ == "__main__":
    n = int(raw_input())
    print solve(n)