#Question : Crafting
#Link to the question:  https://codeforces.com/contest/2055/problem/B

"""Author : Nishant Kumar"""

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    cnt = sum(1 for i in range(n) if a[i] < b[i])
    
    if cnt >= 2:
        print("NO")
    elif cnt == 0:
        print("YES")
    else:
        mx = 0
        mn = float('inf')
        for i in range(n):
            if a[i] < b[i]:
                mx = b[i] - a[i]
            else:
                mn = min(mn, a[i] - b[i])
        
        if mx <= mn:
            print("YES")
        else:
            print("NO")
 
t = int(input())
for _ in range(t):
    solve()

"""Author : Nishant Kumar"""