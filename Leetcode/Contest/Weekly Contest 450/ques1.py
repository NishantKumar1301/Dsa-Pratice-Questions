#Question : Smallest Index With Digit Sum Equal to Index
#Link to the question: https://leetcode.com/contest/weekly-contest-450/problems/smallest-index-with-digit-sum-equal-to-index/description/

class Solution(object):
    # def find_digit_sum(self, n):
    #     ans =0
    #     while n >0:
    #         ans += n%10
    #         n = n%10
    #     return ans
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ans = -1
        # for i in range(len(nums)):
        #     if i==self.find_digit_sum(nums[i]):
        #         return i
        # return ans
        for i, num in enumerate(nums):
            req = sum(int(d) for d in str(num))
            if req == i:
                return i
        return -1
