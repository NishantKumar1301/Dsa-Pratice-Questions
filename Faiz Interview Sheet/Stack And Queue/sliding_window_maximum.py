#Question : Sliding Window Maximum
#Link to the question: https://leetcode.com/problems/sliding-window-maximum/
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n= len(nums)
        queue = deque()
        ans = []
        for i in range(n):
            """
            Step 1 : Window size can not be greater than k , if i-k>=queue[0] then pop elements from left
            Step 2 : if current number is greater than the top then pop all the smaller number
            Step 3 : Append the index i in the queue
            Step 4 : Only when window size become greater than equal to k then append the front of queue to ans i.e if i >=k-1
            """

            #Step 1 :
            while queue and i-k>=queue[0]:
                queue.popleft()
            #step 2 :
            while queue and nums[i]>nums[queue[-1]]:
                queue.pop()
            #step 3 :
            queue.append(i)
            #Step 4 :
            if i>=k-1:
                ans.append(nums[queue[0]])
        return ans