#Question : Count Hills and Valleys in an Array
#Link to the question: https://leetcode.com/problems/count-hills-and-valleys-in-an-array/
class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i,j,n,ans=0,1,len(nums),0
        while j+1<n:
            if (nums[i]>nums[j] and nums[j]<nums[j+1]) or (nums[i]<nums[j] and nums[j]>nums[j+1]):
                ans+=1
                i=j
            else:
                j+=1
        return ans