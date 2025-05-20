#Question : Zero Array Transformation I
#Link to the question: https://leetcode.com/problems/zero-array-transformation-i/description/?envType=daily-question&envId=2025-05-20

class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        n = len(nums)
        arr = [0]*n
        for query in queries:
            arr[query[0]]+=1
            if query[1]+1 <n:
                arr[query[1]+1 ]-=1
        for i in range(1,n):
            arr[i]=arr[i]+arr[i-1]
        for i in range(n):
            if arr[i]<nums[i]:
                return False
        return True
