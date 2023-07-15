#Problem Link -> https://www.hackerrank.com/challenges/python-string-split-and-join/

def split_and_join(line):
    # write your code here
    a=line.split(" ")
    ans="-".join(a)
    return ans

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
