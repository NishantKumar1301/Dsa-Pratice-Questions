#Question : Count Subarrays With Fixed Bounds
#Link to the question: https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/

from collections import deque
class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        ans = 0
        left = 0
        min_queue = deque()
        max_queue = deque()
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                min_queue.clear()
                max_queue.clear()
                left = i + 1
                continue
            while min_queue and nums[min_queue[-1]] >= nums[i]:
                min_queue.pop()
            min_queue.append(i)
            while max_queue and nums[max_queue[-1]] <= nums[i]:
                max_queue.pop()
            max_queue.append(i)
            if nums[min_queue[0]] == minK and nums[max_queue[0]] == maxK:
                start = min(min_queue[0], max_queue[0])
                ans += (start - left + 1)
        return ans

