#Question : Grid Game
#Link to the question: https://leetcode.com/problems/grid-game/description/?envType=daily-question&envId=2025-01-21

class Solution(object):
    def gridGame(self, grid):
        first_row_sum = sum(grid[0])
        second_row_sum =0
        mini = float('inf')
        for j in range(len(grid[0])):
            first_row_sum-=grid[0][j]
            best_for_2 = max(first_row_sum,second_row_sum)
            mini = min(mini,best_for_2)
            second_row_sum+=grid[1][j]
        return mini
        
