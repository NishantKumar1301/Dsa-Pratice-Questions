#Question : Number of Perfect Pairs
#Link to the question: https://leetcode.com/contest/biweekly-contest-163/problems/number-of-perfect-pairs/
class Solution(object):
    def perfectPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = [abs(x) for x in nums]
        arr.sort()
        ans,right,n= 0,0,len(arr)
        for left in range(n):
            if right<left+1:
                right = left+1
            while right<n and arr[right]<=2*arr[left]:
                right+=1
            ans+=(right-left-1)
        return ans