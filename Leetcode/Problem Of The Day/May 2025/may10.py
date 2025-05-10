#Question : Minimum Equal Sum of Two Arrays After Replacing Zeros
#Link to the question: https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/description/?envType=daily-question&envId=2025-05-10

class Solution(object):
    def minSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        sum1=sum2=zero1 =zero2=0
        for num in nums1:
            sum1+=num
            if num == 0:
                sum1+=1
                zero1+=1
        for num in nums2:
            sum2+=num
            if num==0:
                zero2+=1
                sum2+=1
        if (sum1<sum2 and zero1==0) or (sum2<sum1 and zero2==0):
            return -1
        return max(sum1,sum2)
