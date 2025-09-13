#Question : Smallest Absent Positive Greater Than Average
#Link to the question: https://leetcode.com/contest/biweekly-contest-165/problems/smallest-absent-positive-greater-than-average/
class Solution(object):
    def smallestAbsent(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        n = len(nums)
        avg = s//n
        ans = max(1,avg+1)
        s= set(nums)
        while ans in s:
            ans+=1
        return ans
        # s = set(nums) 
        # ans = int(avg)+1
        # while ans in s:
        #     ans += 1
        # if ans<=0:
        #     ans =1
        # return ans©leetcode