#Question : Using a Robot to Print the Lexicographically Smallest String
#Link to the question:https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string
class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        min_char_to_right =['']*n
        min_char_to_right[n-1]= s[n-1]
        for i in range(n-2,-1,-1):
            min_char_to_right[i]= min(s[i],min_char_to_right[i+1])
        
        ans = ""
        stack = []
        for i in range(n):
            stack.append(s[i])
            mini = min_char_to_right[i+1] if i+1< n else s[i]
            while stack and stack[-1]<=mini:
                ans += stack.pop()
        while stack :
            ans +=stack.pop()
        return ans
        