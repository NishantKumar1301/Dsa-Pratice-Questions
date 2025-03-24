#Question : Remove Duplicates from Sorted Array II
#Link to the question: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def removeDuplicates(self, nums):
        k = 0 
        freq = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
            if freq[nums[i]]<=2:
                nums[k]=nums[i]
                k+=1
        return k

