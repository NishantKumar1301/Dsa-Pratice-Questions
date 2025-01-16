#Question : Bitwise XOR of All Pairings
#Link to the question: https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/

class Solution(object):
    def xorAllNums(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        ans = 0
        len1 = len(nums1)
        len2 = len(nums2)
        #If len2 == odd then ans is xored with all the element of nums1
        if len2%2==1:
            for num in nums1:
                ans = ans^num
        #If len1 == odd then ans is xored with all the element of nums2
        if len1%2==1:
            for num in nums1:
                ans = ans^num
        
        return ans


