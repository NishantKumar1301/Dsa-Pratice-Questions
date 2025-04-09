#Question : Find Score of an Array After Marking All Elements
#Link to the question: https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/description/?envType=daily-question&envId=2024-12-13

from heapq import heappush ,heappop
class Solution:
    def findScore(self, nums) -> int:
        pq =[]
        for index,value in enumerate(nums):
            heappush(pq,(value,index))
        seen =set()
        ans =0
        while pq:
            value , curr_index = heappop(pq)
            if curr_index in seen:
                continue
            ans += value
            seen.add(curr_index)
            if curr_index-1>=0:
                seen.add(curr_index-1)
            if curr_index+1 < len(nums):
                seen.add(curr_index+1)
        return ans

        

