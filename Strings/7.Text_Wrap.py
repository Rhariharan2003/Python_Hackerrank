#Problem Link ->  https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true

import textwrap

def wrap(string, max_width):
    i = 0
    s = ""
    for j in range(0,len(string)):
        s = s + string[j]
        i += 1
        if i == max_width:
            s =  s + "\n"
            i = 0
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
