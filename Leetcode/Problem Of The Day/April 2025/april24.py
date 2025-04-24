#Question : Count Complete Subarrays in an Array
#Link to the question: https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/?envType=daily-question&envId=2025-04-24

class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        freq = {}
        n = len(nums)
        right = 0
        s = len(set(nums))
        for left in range(n):
            if left > 0:
                remove = nums[left - 1]
                freq[remove] -= 1
                if freq[remove] == 0:
                    freq.pop(remove)
            while right < n and len(freq) < s:
                add = nums[right]
                freq[add] = freq.get(add, 0) + 1
                right += 1
            if len(freq) == s:
                ans += n - right + 1
        return ans
        