#Question : Minimum Difference in Sums After Removal of Elements
#Link to the question: https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements
import heapq

class Solution(object):
    def minimumDifference(self, nums):
        n = len(nums) // 3
        total = len(nums)
        
        # prefix: smallest sum of n in first 2n
        left_heap = []
        left_sum = 0
        left_sums = [0]*(total+1)
        
        for i in range(2*n):
            heapq.heappush(left_heap, -nums[i])
            left_sum += nums[i]
            if len(left_heap) > n:
                left_sum += heapq.heappop(left_heap) # remove largest (add since it's negative)
            if i >= n-1:
                left_sums[i+1] = left_sum
        
        # suffix: largest sum of n in last 2n
        right_heap = []
        right_sum = 0
        right_sums = [0]*(total+1)
        for i in range(total-1, n-1, -1):
            heapq.heappush(right_heap, nums[i])
            right_sum += nums[i]
            if len(right_heap) > n:
                right_sum -= heapq.heappop(right_heap) # remove smallest
            if i <= 2*n:
                right_sums[i] = right_sum
        
        res = float('inf')
        # i goes from n to 2*n (these are split points)
        for i in range(n, 2*n+1):
            res = min(res, left_sums[i] - right_sums[i])
        
        return res
