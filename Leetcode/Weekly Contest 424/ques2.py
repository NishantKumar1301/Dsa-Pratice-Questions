#Question2 : Zero Array Transformation I
# Link to the Question : https://leetcode.com/problems/zero-array-transformation-i/description/

class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        n = len(nums)
        sweep_line = [0]*n
        #Calculating the sweep line
        for query in queries:
            sweep_line[query[0]]+=1
            if query[1]+1 <n:
                sweep_line[query[1]+1 ]-=1
                
        #Step 2 : Finding the max capacity by finding the prefix sum of the sweep line
        for i in range(1,n):
            sweep_line[i]=sweep_line[i]+sweep_line[i-1]
        
        #Step3 : Return false if nums[i]>sweep_line[i]
        for i in range(n):
            if sweep_line[i]<nums[i]:
                return False