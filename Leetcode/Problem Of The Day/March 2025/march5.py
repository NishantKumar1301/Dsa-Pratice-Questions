#Question : Count Total Number of Colored Cells
#Link to the question: https://leetcode.com/problems/count-total-number-of-colored-cells/description/?envType=daily-question&envId=2025-03-05

class Solution:
    def coloredCells(self, n) :
        return 1 + 4 * (n * (n - 1) // 2)

class Solution2:
    def coloredCells(self, n) :
        count = 1
        jump_size = 4
        while n > 1:
            count += jump_size
            jump_size += 4
            n -= 1
        return count

