#Question : Distribute Candies Among Children II
#Link to the question: https://leetcode.com/problems/distribute-candies-among-children-ii/?envType=daily-question&envId=2025-06-01
class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
        minCand1 = max(0,n-2*limit)
        maxCand1 = min(n,limit)
        #Fixed the minimum and maximum for the candidate 1 , so it behaves like 2 candidate only
        ans =0
        for i in range(minCand1,maxCand1+1):
            #For two candidate , min = max(0,n-limit), max = min(limit , n) , ans = max-min+1
            #Now new N = n-i , removed the first candidate
            N = n-i
            minCand2 = max(0,N-limit)
            maxCand2 = min(N,limit)
            ans += (maxCand2-minCand2+1)
        return ans



