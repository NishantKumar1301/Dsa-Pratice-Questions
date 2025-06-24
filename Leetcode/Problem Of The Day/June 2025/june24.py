#Question : Find All K-Distant Indices in an Array
#Link to the question:  https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        # ans =[]
        s= set()
        n = len(nums)
        for i in range(n):
            if nums[i]==key:
                start = max(0,i-k)
                end = min(n-1,i+k)
                for j in range(start,end+1):
                    if j not in s:
                        s.add(j)
        return sorted(s)
