#Question : Koko Eating Bananas
#Link to the question: https://leetcode.com/problems/koko-eating-bananas/
import math
class Solution(object):
    def caculateTime(self,arr,time):
        total = 0
        n = len(arr)
        for i in range(n):
            total+=math.ceil(arr[i]/float(time))
        return total

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        #The range of the number will be from 1 to max(piles) , then apply binary search on ans
        n = len(piles)
        low = 1
        high = max(piles)
        while low<=high :
            mid = low+(high-low)//2
            total = self.caculateTime(piles,mid)
            if total<=h:
                high = mid-1
            else:
                low = mid+1
        return low