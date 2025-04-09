#Question : Maximum Value of an Ordered Triplet I
#Link to the question: https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/submissions/1595419199/?envType=daily-question&envId=2025-04-03

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


#####For smaller testcases 

class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :r type: int
        """
        n =len(nums)
        ans =0
        for i in range(n-2):
            for j in range(n-1):
                for k in range(n):
                    ans = max(ans,(nums[i]-nums[j])*nums[k])
        return ans

