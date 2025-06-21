#Question : Minimum Adjacent Swaps to Alternate Parity
#Link to the question:  https://leetcode.com/contest/biweekly-contest-159/problems/minimum-adjacent-swaps-to-alternate-parity/

class Solution(object):
    def numberOfSwap(self,arr):
        cnt = 0
        n = len(arr)
        for i in range(n):
            cnt+=abs(arr[i]-(2*i))
        return cnt

    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even = []
        odd = []
        n = len(nums)
        ans = float('inf')
        for i in range(n):
            if nums[i]%2==0:
                even.append(i)
            else:
                odd.append(i)
        e, o = len(even),len(odd)
        if abs(e-o)>1:
            return -1
        if e>=o:
            ans = min(ans, self.numberOfSwap(even))
        if o>=e:
            ans = min(ans,self.numberOfSwap(odd))

        return ans