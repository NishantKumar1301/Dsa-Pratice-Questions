#Question : Find Subsequence of Length K With the Largest Sum
#Link to the question:  https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        if n ==k:
            return nums
        temp = [(i,val) for i,val in enumerate(nums)]
        temp.sort(key = lambda x:x[1], reverse=True)
        # Take top k elements, then sort them by index to preserve order
        temp = sorted(temp[:k],key = lambda x:x[0])
        ans = [val for idx,val in temp]
        return ans