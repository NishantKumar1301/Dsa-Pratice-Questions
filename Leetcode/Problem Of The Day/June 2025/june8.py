#Question : Lexicographical Numbers
#Link to the question:https://leetcode.com/problems/lexicographical-numbers/
class Solution(object):
    def helper(self,ans,curr,n):
        if curr>n:
            return 
        ans.append(curr)
        for nxt in range(10):
            nextnum = curr*10+nxt
            if nextnum>n:
                return 
            self.helper(ans,nextnum,n)

    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans =[]
        for num in range(1,10):
            self.helper(ans,num,n)
        return ans
        