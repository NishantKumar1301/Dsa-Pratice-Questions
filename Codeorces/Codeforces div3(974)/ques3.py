#Link to the problem : https://codeforces.com/contest/2014/problem/C
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    if n<=2:
        print("-1")
        continue 
    total_sum = sum(x for x in arr)
    arr.sort()
    req = arr[n//2]*2*n+ 1
    if total_sum >= req:
        print("0")
    else:
        print(req-total_sum)