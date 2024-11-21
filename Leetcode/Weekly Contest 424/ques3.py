#Question3 : Zero Array Transformation II
#Link to the question : https://leetcode.com/contest/weekly-contest-424/problems/zero-array-transformation-ii/description/
class Solution(object):
    def isPossible(self, k, queries, nums):
        n = len(nums)
        sweep_line = [0] * (n + 1)
        
        for i in range(k):
            sweep_line[queries[i][0]] += queries[i][2]
            if queries[i][1] + 1 < n:
                sweep_line[queries[i][1] + 1] -= queries[i][2]
        
        for i in range(1, n):
            sweep_line[i] += sweep_line[i - 1]
        
        for i in range(n):
            if sweep_line[i] < nums[i]:
                return False

        return True

    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        low = 0
        high = len(queries)
        ans = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            if self.isPossible(mid, queries, nums):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
