#Question : Merge Two 2D Arrays by Summing Values
#Link to the question: https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/?envType=daily-question&envId=2025-03-02

class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :r type: List[List[int]]
        """
        freq = {}

        for nums in nums1:
            freq[nums[0]] = nums[1]

        for nums in nums2:
            freq[nums[0]] = freq.get(nums[0], 0) + nums[1]

        ans = []
        for key, value in sorted(freq.items()):
            ans.append([key, value])

        return ans
        

