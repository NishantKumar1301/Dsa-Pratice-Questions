#Question : Array Coloring
#Link to the question: https://codeforces.com/contest/1857/problem/A

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    sum_ = sum(arr)
    if sum_%2==0:
        print("YES")
    else:
        print("No")
