#Question : Maximum Unique Subarray Sum After Deletion
#Link to the question: https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/
class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s= set()
        neg_count=0
        for num in nums:
            if num>0:
                s.add(num)
            if num<0:
                neg_count+=1
        ans = 0
        if len(nums)==neg_count:
            return max(nums)
        for num in s:
            ans+=num
        return ans
        