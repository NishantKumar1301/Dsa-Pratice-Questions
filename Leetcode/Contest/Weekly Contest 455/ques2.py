#Question : Inverse Coin Change
#Link to the question:  https://leetcode.com/contest/weekly-contest-455/problems/inverse-coin-change/

class Solution(object):
    def findCoins(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n,ans  = len(arr),[]
        ways = [0]*(n+1)
        ways[0]=1
        for i in range(1,n+1):
            if ways[i]!=arr[i-1]:
                ans.append(i)
                for j in range(i,n+1):
                    ways[j]+=ways[j-i]

        for i in range(n):
            if ways[i+1]!=arr[i]:
                return []

        return ans