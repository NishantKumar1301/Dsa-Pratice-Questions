#Question : Maximum Value of an Ordered Triplet I
#Link to the question: https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/?envType=daily-question&envId=2025-04-02

class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :r type: int
        """
        n = len(nums)
        ans =0
        max_diff =0
        max_left =0
        ans =0
        for i in range(n):
            ans = max(ans,max_diff*nums[i])
            max_diff = max(max_diff,max_left-nums[i])
            max_left= max(max_left,nums[i])
        return ans

