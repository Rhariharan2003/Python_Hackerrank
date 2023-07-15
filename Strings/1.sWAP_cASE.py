#Problem Link -> https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    ans = s.swapcase()
    return ans

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
