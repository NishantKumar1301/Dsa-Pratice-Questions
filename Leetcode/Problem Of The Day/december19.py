#Question : Max Chunks To Make Sorted 
#Link to the question: https://leetcode.com/problems/max-chunks-to-make-sorted/description/?envType=daily-question&envId=2024-12-19

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        maxi = float("-inf")
        ans =0
        for i in range(len(arr)):
            maxi = max(maxi,arr[i])
            if i==maxi:
                ans+=1
        return ans

        

