__author__ = 'deveshbajpai'

'''
Problem Url: http://codeforces.com/problemset/problem/474/A

Algorithm: Maintain the actual keys of a keyboard. For a given input, iterate over it and firstly check which line
of actual keys is it. Secondly, obtain the index of it in the actual keys line. Thirdly, as per Left or Right, increment
or decrement the desired index. Not sure if that was required, but this solution takes care of circular references too.
E.g. if the input was 'a' and direction was R, output will pick ';' for it.
'''


keys = ["qwertyuiop",
"asdfghjkl;",
"zxcvbnm,./"]


def solve(direction,input):
    keys_curr = []
    index = 0
    output = ""
    for i in input:
        #check which keys line input is in
        if(i in keys[0]):
            keys_curr = keys[0]
        elif(i in keys[1]):
            keys_curr = keys[1]
        elif(i in keys[2]):
            keys_curr = keys[2]

        #get index of input character in keys line
        index = keys_curr.index(i)

        #choose the correct character as per the direction
        if(direction=='L'):
            output += keys_curr[(index+1)%10]
        elif(direction=='R'):
            if(index-1==-1):
                index = 10
            output += keys_curr[index-1]
    return output

if __name__ == "__main__":

    direction = raw_input()
    input = raw_input()
    print solve(direction,input)