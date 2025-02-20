#Question : Find Unique Binary String
#Link to the question: https://leetcode.com/problems/find-unique-binary-string/description/?envType=daily-question&envId=2025-02-20

class Solution(object):

    def __init__(self):
        self.ans = ""

    def build(self,s,curr,n):
        if len(curr)==n:
            if curr not in s:
                self.ans = curr
                return True
            return False
        
        if self.build(s,curr+'0',n):
            return True
        if self.build(s,curr+'1',n):
            return True
        return False

    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :r type: str
        """
        n = len(nums)
        s = set(nums)
        self.build(s,"",n)
        return self.ans
        

