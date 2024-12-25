#Question : Coin Transformation
#Link to the question: https://codeforces.com/contest/2043/problem/A

"""Author : Nishant Kumar"""
 
def solve():
    n = int(input())
    k = 0
    curr = 1
    while curr * 4 <= n:
        curr *= 4
        k += 1
    print(1<<k)
    
 
 
 
for _ in range(int(input())):
    solve()
 
"""Author : Nishant Kumar"""