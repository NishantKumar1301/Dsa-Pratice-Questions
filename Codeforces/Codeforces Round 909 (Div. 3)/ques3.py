#Question : Yarik and Array
#Link to the question: https://codeforces.com/contest/1899/problem/C
 
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    ans,total = float('-inf'),0
    for i in range(n):
        total+=arr[i]
        ans = max(ans,total)
        if i<n-1 and (abs(arr[i])%2==abs(arr[i+1])%2):
            total =0
        if total<0:
            total =0
    print(ans)