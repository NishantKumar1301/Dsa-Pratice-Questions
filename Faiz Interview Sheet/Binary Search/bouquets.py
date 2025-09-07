#Question : Minimum Number of Days to Make m Bouquets
#Link to the question: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
class Solution(object):
    def solve(self,arr,day,m,k):
        cnt =0
        noOfBucket = 0
        n = len(arr)
        for i in range(n):
            if arr[i]<=day:
                cnt+=1
            else:
                noOfBucket+=(cnt//k)
                cnt=0
        noOfBucket+=(cnt//k)
        if noOfBucket>=m:
            return True
        else:
            return False

    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        n = len(bloomDay)
        total = m*k
        if total>n:
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        while low<=high:
            mid = low+(high-low)//2
            if not self.solve(bloomDay,mid,m,k):
                low = mid+1
            else:
                high = mid -1
        return low