#Question : Queue Sort
#Link to the question: https://codeforces.com/contest/1899/problem/E

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    mini = min(arr)
    ind=-1
    for i in range(n):
        if arr[i]== mini:
            ind= i
            break
    
    if arr[ind:]==sorted(arr[ind:]):
        print(ind)
    else:
        print("-1")

