#Question : Divide Array Into Equal Pairs
#Link to the question: https://leetcode.com/problems/divide-array-into-equal-pairs/description/?envType=daily-question&envId=2025-03-17

class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        for value in freq.values():
            if value &1 !=0: #value %2 !=0
                return False
        return True
        

