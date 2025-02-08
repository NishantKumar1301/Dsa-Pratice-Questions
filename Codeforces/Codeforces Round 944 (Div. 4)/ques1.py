#Question : My First Sorting Problem
#Link to the question: https://codeforces.com/contest/1971/problem/A

for _ in range(int(input())):
    a,b = map(int,input().split())
    mini ,maxi = min(a,b),max(a,b)
    print(f"{mini} {maxi}")

