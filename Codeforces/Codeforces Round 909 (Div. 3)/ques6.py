#Question : Alex's whims
#Link to the question: https://codeforces.com/contest/1899/problem/F

for _ in range(int(input())):
    n,q = map(int,input().split())
    for i in range(1,n):
        print(i,i+1)
    prev=n-1
    for _ in range(q):
        d= int(input())
        if d==prev:
            print("-1 -1 -1")
        else:
            print(n,prev,d)
            prev=d