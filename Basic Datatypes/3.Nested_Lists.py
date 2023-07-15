#   Problem Link -> https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

dict = {}
l = list()
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in dict:
            dict[score].append(name)
        else:
            dict[score]=[name]
        if score not in l:
            l.append(score)
    
    p = min(l)
    l.remove(p)
    m = min(l)
    dict[m].sort()
    print(dict)
    for  i in dict[m]:
        print(i)
