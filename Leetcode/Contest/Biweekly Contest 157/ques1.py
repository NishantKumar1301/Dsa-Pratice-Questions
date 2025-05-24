#Question : Sum of Largest Prime Substrings
#Link to the question: https://leetcode.com/contest/biweekly-contest-157/problems/sum-of-largest-prime-substrings/?slug=sum-of-largest-prime-substrings&region=global_v2

class Solution(object):
    def is_prime(self,n):
        
        if n<=1:
            return False
        if n==2:
            return True
        if n%2==0:
            return False
        for i in range(3,int(n**0.5)+1,2):
            if n % i==0:
                return False
        return True
        
    def sumOfLargestPrimes(self, s):
        """
        :type s: str
        :rtype: int
        """
        prime,n = set(),len(s)
        for i in range(n):
            for j in range(i+1,n+1):
                num = int(s[i:j])
                if self.is_prime(num):
                    prime.add(num)
        sorted_prime = sorted(prime,reverse=True)
        top_prime = sorted_prime[:3]
        return sum(top_prime)