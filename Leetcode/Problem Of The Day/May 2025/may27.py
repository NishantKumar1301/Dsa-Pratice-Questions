#Question : Divisible and Non-divisible Sums Difference
#Link to the question: https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/?envType=daily-question&envId=2025-05-27

class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        sum1=sum2=0
        for i in range(1,n+1):
            if i%m==0:
                sum2+=i
            else:
                sum1+=i
        return sum1-sum2
