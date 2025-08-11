#Question : Range Product Queries of Powers
#Link to the question: https://leetcode.com/problems/range-product-queries-of-powers/
MOD = 10**9+7
class Solution(object):
    def productQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        powers ,ans = [],[]
        for i in range(32):
            #If ith  bit of n is set then store its power in the power
            if (n & (1<<i))!=0:
                powers.append(1<<i) # power of i = 1<<i
        
        for query in queries:
            start,end = query[0],query[1]
            prod =1
            for i in range(start,end+1):
                prod = (prod*powers[i]) % MOD
            ans.append(prod)
        return ans
