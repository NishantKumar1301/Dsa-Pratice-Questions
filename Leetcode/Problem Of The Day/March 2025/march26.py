#Question : Minimum Operations to Make a Uni-Value Grid
#Link to the question: https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/description/?envType=daily-question&envId=2025-03-26

class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :r type: int
        """
        arr = []
        rem = grid[0][0]%x
        for row in grid:
            for num in row:
                if num%x!=rem:
                    return -1
                arr.append(num)
        
        arr.sort()
        mid = len(arr)//2
        ans =0
        for num in arr:
            ans +=abs(num-arr[mid])//x
        return ans



