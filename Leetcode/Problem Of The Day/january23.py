#Question : Count Servers that Communicate
#Link to the question: https://leetcode.com/problems/count-servers-that-communicate/description/?envType=daily-question&envId=2025-01-23

class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n , m = len(grid) , len(grid[0])
        rows= [0]*n 
        col = [0]*m
        ans =0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    rows[i]+=1
                    col[j]+=1
                    ans +=1 

        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and (rows[i]==1 and col[j]==1):
                    ans-=1
        return ans


