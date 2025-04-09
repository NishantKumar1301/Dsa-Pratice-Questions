#Question : Minimum Length of String After Operations
#Link to the question: https://leetcode.com/problems/minimum-length-of-string-after-operations/

class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq ={}
        ans =0
        for char in s:
            if char in freq:
                freq[char]+=1
            else:
                freq[char]=1
        for value in freq.values():
            if value==0 or value==1 or value ==2:
                ans+=value
            elif value%2==0:
                ans+=2
            else:
                ans+=1
        return ans

        
