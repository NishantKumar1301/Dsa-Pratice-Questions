#Question : Next Greater Element I
#Link to the question:  https://leetcode.com/problems/next-greater-element-i/

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n= len(nums2)
        nge = {} #Stores the next greater element of every num in nums2
        stack = []
        for i in range(n-1,-1,-1):
            while len(stack)>0 and nums2[i]>=stack[-1]:
                stack.pop()
            if len(stack)==0:
                nge[nums2[i]]=-1
            else:
                nge[nums2[i]]=stack[-1]
            stack.append(nums2[i])
        #Now for every element in nums1 find the nextgreatest element from the dictionary
        ans = []
        for num in nums1:
            ans.append(nge[num])
        return ans
