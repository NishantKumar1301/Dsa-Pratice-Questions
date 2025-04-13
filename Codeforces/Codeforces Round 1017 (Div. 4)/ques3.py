#Question : Brr Brrr Patapim
#Link to the question: https://codeforces.com/contest/2094/problem/C

# Contest: Codeforces Round 1017 (Div. 4)
# Date: April 13, 2025
# Author: Nishant Kumar
 
def solve():
    n = int(input())
    grid = [list(map(int,input().split())) for _ in range(n)]
    dp=[0]*(2*n+1)
    for i in range(n):
        for j in range(n):
            total = i+j+2
            if dp[total]==0:
                dp[total]=grid[i][j]
    
    visited = [False]*(2*n+1)
    for i in range(2*n+1):
        visited[dp[i]]=True
    
    ans =0
    for i in range(1,2*n+1):
        if not visited[i]:
            ans = i
            break
    dp[1]=ans
    print(" ".join(map(str, dp[1:2 * n + 1])))
    
if __name__ == "__main__":
    for _ in range(int(input())):
        solve()

# Author: Nishant Kumar

