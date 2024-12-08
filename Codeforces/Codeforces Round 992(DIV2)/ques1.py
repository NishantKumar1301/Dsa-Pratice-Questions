#Question : Game of Division
#Link to the question: https://codeforces.com/contest/2040/problem/A

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    res = -1
 
    for i in range(n):
        ans = True
        for j in range(n):
            if i!=j:
                if abs(arr[i] - arr[j]) % k == 0:
                    ans =False
 
        if ans:
            res = i + 1
 
    if res != -1:
        print("YES")
        print(res)
    else:
        print("NO")

