#Question : Line Breaks
#Link to the question: https://codeforces.com/contest/2050/problem/A


"""Author : Nishant Kumar"""

def solve():
    n,m = map(int,input().split())
    arr = [input().strip() for _ in range(n)]
    ans=0
    for i in range(n):
        if len(arr[i])<=m:
            ans+=1
            m-=len(arr[i])
        else:
            break
    print(ans)


for _ in range(int(input())):
    solve()

"""Author : Nishant Kumar"""