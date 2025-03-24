#Question : Majority Element
#Link to the question: https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def majorityElement(self, nums):
        ans =0
        n = len(nums)
        limit = n//2
        freq = {}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for num in nums:
            if freq[num]> limit:
                ans = num
                break
        return ans



