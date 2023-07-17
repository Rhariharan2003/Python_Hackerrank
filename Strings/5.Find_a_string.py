#Problem Link -> https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true

def count_substring(string, sub_string):
    n = len(sub_string)
    
    c = 0
    for  i in range(0,len(string)):
        
        ans = string[i:(i+n)]
        
        if(ans == sub_string):
             c += 1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
