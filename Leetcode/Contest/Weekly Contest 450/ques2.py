#Question : Minimum Swaps to Sort by Digit Sum
#Link to the question: https://leetcode.com/contest/weekly-contest-450/problems/minimum-swaps-to-sort-by-digit-sum/description/?slug=smallest-index-with-digit-sum-equal-to-index&region=global_v2


class Solution(object):
    def digit_sum(self,n):
        return sum(int(d) for d in str(n))
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n,ans= len(nums), 0
        visited  = [False]*n
        arr = [(self.digit_sum(p), p, i) for i, p in enumerate(nums)]
        arr.sort(key=lambda x: (x[0], x[1]))
        for i in range(n):
            if visited[i] or arr[i][2]==i:
                continue
            length,j = 0,i
            while not visited[j]:
                visited[j]=True
                j = arr[j][2]
                length+=1
            if length>1:
                ans+=length-1
        return ans
