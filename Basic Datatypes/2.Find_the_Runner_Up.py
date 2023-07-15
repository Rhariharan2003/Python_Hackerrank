#Problem Link -> https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
arr = list(arr)

maxi = arr[0]

for i in range(1,n):
    if arr[i] > maxi:
        maxi = arr[i]
 
c = arr.count(maxi)
for  i in range(c):
    arr.remove(maxi)      
print(max(arr))
