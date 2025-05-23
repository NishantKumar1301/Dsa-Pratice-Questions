#Question : Find the Maximum Sum of Node Values
#Link to the question: https://leetcode.com/problems/find-the-maximum-sum-of-node-values/description/?envType=daily-question&envId=2025-05-23

class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        """
        :type nums: List[int]
        :type k: int
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        arr = [(nums[i] ^ k) - nums[i] for i in range(n)]
        ans = sum(nums)
        arr.sort(reverse=True)
        for i in range(0, n, 2):
            if i + 1 == n:
                break
            sum_ = arr[i] + arr[i + 1]
            if sum_ > 0:
                ans += sum_
        return ans
        
