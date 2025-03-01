#Question : Transform Array by Parity
#Link to the question: https://leetcode.com/contest/biweekly-contest-151/problems/transform-array-by-parity/description/?slug=find-minimum-cost-to-remove-array-elements&region=global_v2

class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :r type: List[int]
        """
        n = len(nums)
        for i in range(n):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        nums.sort()
        return nums

