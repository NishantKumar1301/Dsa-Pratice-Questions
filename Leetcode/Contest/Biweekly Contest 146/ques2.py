#Question : Count Paths With the Given XOR Value
#Link to the question: https://leetcode.com/contest/biweekly-contest-146/problems/count-paths-with-the-given-xor-value/description/

class Solution(object):
    def countPathsWithXorValue(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        REM = int(1e9 + 7)
        m, n = len(grid), len(grid[0])
        
        dp_array = [[{} for _ in range(n)] for _ in range(m)]
        dp_array[0][0][grid[0][0]] = 1  

        for i in range(m):
            for j in range(n):
                for xor, c in dp_array[i][j].items():
                    if j + 1 < n: 
                        new_xor_value = xor ^ grid[i][j + 1]
                        if new_xor_value not in dp_array[i][j + 1]:
                            dp_array[i][j + 1][new_xor_value] = 0
                        dp_array[i][j + 1][new_xor_value] += c
                        dp_array[i][j + 1][new_xor_value] %= REM

                    if i + 1 < m:  
                        new_xor_value = xor ^ grid[i + 1][j]
                        if new_xor_value not in dp_array[i + 1][j]:
                            dp_array[i + 1][j][new_xor_value] = 0
                        dp_array[i + 1][j][new_xor_value] += c
                        dp_array[i + 1][j][new_xor_value] %= REM

        return dp_array[m - 1][n - 1].get(k, 0)


