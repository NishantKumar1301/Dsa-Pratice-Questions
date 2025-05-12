#Question : Finding 3-Digit Even Numbers
#Link to the question: https://leetcode.com/problems/finding-3-digit-even-numbers/description/?envType=daily-question&envId=2025-05-12

class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = set()
        n = len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i==j or j==k or k==i:
                        continue
                    num = digits[i]*100 + digits[j]*10+digits[k]
                    if num>=100 and num%2==0:
                        s.add(num)
        ans = sorted(list(s))
        return ans

