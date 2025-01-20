#Question : Chocolate Pickup
#Link to the question: https://www.naukri.com/code360/problems/chocolate-pickup_3125885?leftPanelTabValue=PROBLEM

#Method 1 : using Memoisation 

class Solution:
    def helper(self,i,j1,j2,n,m,grid,dp):
        if j1<0 or j1>=m or j2<0 or j2>=m:
            return int(-1e9)
        if i==n-1:
            if j1==j2:
                return grid[i][j1]
            else:
                return grid[i][j1]+grid[i][j2]
        if dp[i][j1][j2]!=-1:
            return dp[i][j1][j2]
        maxi = float('-inf')
        for dy1 in range(-1,2):
            for dy2 in range(-1,2):
                ans =0
                if j1==j2:
                    ans = grid[i][j1]+self.helper(i+1,j1+dy1,j2+dy2,n,m,grid,dp)
                else:
                    ans = grid[i][j1]+grid[i][j2]+self.helper(i+1,j1+dy1,j2+dy2,n,m,grid,dp)
                    
                maxi = max(ans,maxi)
        dp[i][j1][j2]=maxi
        return dp[i][j1][j2]
        
    def solve(self, n, m, grid):
        # Code here
        dp=[[[-1]*m for _ in range(m)]for _ in range(n)]
        return self.helper(0,0,m-1,n,m,grid,dp)
    
#Method2 : Using Tabulation 

def maximumChocolates(r: int, c: int, grid) -> int:
    # write your code here
    #Grid = R*C*c
    dp =[[[0]*c for _ in range(c)]for _ in range(r)]
    for j1 in range(c):
        for j2 in range(c):
            if j1==j2:
                dp[r-1][j1][j2]=grid[r-1][j1]
            else:
                dp[r-1][j1][j2]=grid[r-1][j1]+grid[r-1][j2]
    for i in range(r-2,-1,-1):
        for j1 in range(c):
            for j2 in range(c):
                maxi = float('-inf')
                for dy1 in range(-1,2):
                    for dy2 in range(-1,2):
                        ans =0
                        if j1==j2:
                            ans = grid[i][j1]
                        else:
                            ans = grid[i][j1]+grid[i][j2]
                        if (j1+dy1<0 or j1+dy1>=c) or(j2+dy2<0 or j2+dy2>=c):
                            ans += int(-1e9)
                        else:
                            ans+=dp[i+1][j1+dy1][j2+dy2]
                        maxi = max(maxi,ans)
                dp[i][j1][j2]=maxi
    return dp[0][0][c-1]


