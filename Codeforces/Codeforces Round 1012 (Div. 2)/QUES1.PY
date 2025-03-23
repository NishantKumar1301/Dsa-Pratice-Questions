#Question : Treasure Hunt
#Link to the question: https://codeforces.com/contest/2090/problem/A

for _ in range(int(input())):
    x, y, z = map(int, input().split())
    sum_ =0
    sum_ = x+y
    rem = z%sum_ 
    if rem>=x:
        print("YES")
    else:
        print("NO")

