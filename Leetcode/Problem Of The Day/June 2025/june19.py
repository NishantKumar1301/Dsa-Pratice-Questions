#Question : Partition Array Such That Maximum Difference Is K
#Link to the question: https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/
class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        ans = 1
        mini = nums[0]
        for  i in range(1,len(nums)):
            if nums[i]-mini>k:
                mini = nums[i]
                ans+=1
        return ans
