#Question : Replace Non-Coprime Numbers in Array
#Link to the question: https://leetcode.com/problems/replace-non-coprime-numbers-in-array
class Solution(object):
    def gcd(self,a,b):
        while b:
            a,b = b, a%b
        return a

    def replaceNonCoprimes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        for num in nums:
            while stack:
                prev = stack[-1]
                curr = num
                Gcd = self.gcd(prev,curr)
                if Gcd==1:
                    break
                stack.pop()
                Lcm = (prev*curr)/Gcd
                num = Lcm
            stack.append(num)
        return stack