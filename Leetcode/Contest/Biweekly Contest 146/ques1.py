#Question :  Count Subarrays of Length Three With a Condition
#Link to the question:  https://leetcode.com/contest/biweekly-contest-146/problems/count-subarrays-of-length-three-with-a-condition/description/

class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in range(len(nums)-2):
            f,m,l=nums[i],nums[i+1],nums[i+2]
            if f+l==m/2.0 :
                count+=1

        return count
            


