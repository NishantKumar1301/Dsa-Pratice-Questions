#Question : Remove Element
#Link to the question: https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def removeElement(self, nums, val):
        idx = 0
        for num in nums:
            if num != val:
                nums[idx]=num
                idx+=1
        return idx

