#Question : Check if Grid can be Cut into Sections
#Link to the question: https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/description/?envType=daily-question&envId=2025-03-25

class Solution:
    def helper(self,rectangles, dim):
            cnt = 0
            rectangles.sort(key=lambda rect: rect[dim])
            furthest_end = rectangles[0][dim + 2]
            for i in range(1, len(rectangles)):
                rect = rectangles[i]
                if furthest_end <= rect[dim]:
                    cnt += 1
                furthest_end = max(furthest_end, rect[dim + 2])
            return cnt >= 2

    def checkValidCuts(self, n, rectangles):
        return self.helper(rectangles, 0) or self.helper(rectangles, 1)