#Question : Best Time to Buy and Sell Stock V
#Link to the question: https://leetcode.com/contest/biweekly-contest-158/problems/best-time-to-buy-and-sell-stock-v/
class Solution(object):
    def maximumProfit(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mini = float('-inf')
        ans = [mini] * (k + 1)
        arr1,arr2 = [mini] * (k + 1),[mini] * (k + 1)
        ans[0] = 0 
        for num in nums:
            arr3,arr4,arr5 = ans[:],arr1[:],arr2[:]
            for i in range(k):
                if arr3[i] != mini:
                    arr1[i] = max(arr1[i], arr3[i] - num)  
                    arr2[i] = max(arr2[i], arr3[i] + num)   
            for i in range(1, k + 1):
                if arr4[i - 1] != mini:
                    ans[i] = max(ans[i], arr4[i - 1] + num)     
                if arr5[i - 1] != mini:
                    ans[i] = max(ans[i], arr5[i - 1] - num)       
        return max(ans) 