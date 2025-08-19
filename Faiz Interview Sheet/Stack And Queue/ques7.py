#Question : Next Greater Element II
#Link to the question: https://leetcode.com/problems/next-greater-element-ii/
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #In case of circular array we create a virtual array of double size
        # Real index = i % n
        n = len(nums)
        nge = [-1]*n
        stack = []
        for i in range(2*n-1,-1,-1):#Last index = 2*n-1
            while len(stack)>0 and nums[i%n]>=stack[-1]:
                stack.pop()
            if i<n:
                if len(stack)==0:
                    nge[i]=-1
                else:
                    nge[i]= stack[-1]
            stack.append(nums[i%n])
        return nge