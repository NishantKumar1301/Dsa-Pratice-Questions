#Question : Minimum Removals to Balance Array
#Link to the question: https://leetcode.com/contest/biweekly-contest-162/

class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n, cnt ,left = len(nums),0,0
        for right in range(n):
            while nums[right]>nums[left]*k:
                left+=1
            cnt = max(cnt,right-left+1)
        return n - cnt
        