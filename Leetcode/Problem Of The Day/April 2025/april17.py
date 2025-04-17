#Question : Count Equal and Divisible Pairs in an Array
#Link to the question: https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/description/?envType=daily-question&envId=2025-04-17

class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        ans =0
        for i in range(n):
            for j in range(i,n):
                if nums[i]==nums[j]:
                    if (i*j) % k==0 and i<j:
                        ans+=1
        return ans

