#Question : Find Missing and Repeated Values
#Link to the question: https://leetcode.com/problems/find-missing-and-repeated-values/description/?envType=daily-question&envId=2025-03-06

class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        freq = {}

        for row in grid:
            for num in row:
                freq[num] = freq.get(num, 0) + 1

        for num in range(1, n * n + 1):
            if num not in freq:
                missing = num  
            elif freq[num] == 2:
                repeat = num  

        return [repeat, missing]
        

