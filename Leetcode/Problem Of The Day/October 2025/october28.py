#Question : Make Array Elements Equal to Zero
#Link to the question: https://leetcode.com/problems/make-array-elements-equal-to-zero/
class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefix_sum =[0]*n
        prefix_sum[0]= nums[0]
        for i in range(1,n):
            prefix_sum[i]=prefix_sum[i-1]+nums[i]
        ans = 0
        for i in range(n):
            if nums[i]==0:
                left_sum = prefix_sum[i-1]
                right_sum = prefix_sum[n-1]-prefix_sum[i-1]
                diff = abs(left_sum-right_sum)
                if diff==0:
                    ans +=2
                elif diff ==1:
                    ans +=1
        return ans