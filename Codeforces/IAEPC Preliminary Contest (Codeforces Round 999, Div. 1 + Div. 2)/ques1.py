#Question : Kevin and Arithmetic
#Link to the question: https://codeforces.com/contest/2061/problem/A

"""Author : Nishant Kumar"""

def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    even =odd=0
    for num in arr:
        if num%2==0:
            even+=1
        else:
            odd+=1
    if even ==0:
        print(n-1)
    else:
        print(1+odd)


for _ in range(int(input())):
    solve()

"""Author : Nishant Kumar"""

