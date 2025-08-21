#Question : Remove K Digits
#Link to the question: https://leetcode.com/problems/remove-k-digits/

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for char in num:
            while len(stack)>0 and k >0 and int(char)<int(stack[-1]):
                stack.pop()
                k-=1
            stack.append(char)
        while k>0:
            stack.pop()
            k-=1
        if len(stack)==0:
            return "0"
        ans = "".join(stack)
        # idx = 0 #for storing the index of first non zero element
        # while idx<len(ans) and ans[idx]=='0':
        #     idx+=1
        # if idx<len(ans):
        #     return  ans[idx:]
        # else:
        #     return "0"
        ans = ans.lstrip('0')
        return ans if len(ans)>0 else "0"