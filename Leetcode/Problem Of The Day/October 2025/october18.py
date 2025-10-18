#Question : Maximum Number of Distinct Elements After Operations
#Link to the question: https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/
class Solution(object):
    def maxDistinctElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mini = min(nums)
        maxi = max(nums)
        acc_value = maxi - mini + 1
        arr = [0] * acc_value
        for num in nums:
            arr[num - mini] += 1
        ans = 0
        l = float('-inf')
        for i in range(acc_value):
            while arr[i] > 0:
                num = i + mini
                start = max(num - k, l + 1)
                if start <= num + k:
                    l = start  
                    ans += 1
                    arr[i] -= 1  
                else:
                    break
        return ans