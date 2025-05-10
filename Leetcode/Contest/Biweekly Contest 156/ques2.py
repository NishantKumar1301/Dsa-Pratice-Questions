#Question : Minimum Operations to Convert All Elements to Zero
#Link to the question: https://leetcode.com/contest/biweekly-contest-156/problems/minimum-operations-to-convert-all-elements-to-zero/description/?slug=find-most-frequent-vowel-and-consonant&region=global_v2

class Solution:
    def solve(self, nums):
        n = len(nums)
        stack = []
        ans = 0
        for i in range(n):
            if nums[i] == 0:
                stack.append(nums[i])
                continue
            while stack and nums[i] < stack[-1]:
                stack.pop()
            if not stack or nums[i] != stack[-1]:
                stack.append(nums[i])
                ans+= 1
        return ans

    def minOperations(self, nums):
        return self.solve(nums)
