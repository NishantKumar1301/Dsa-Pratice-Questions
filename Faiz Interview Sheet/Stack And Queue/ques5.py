#Question : Infix to Postfix
#Link to the question: https://www.geeksforgeeks.org/problems/infix-to-postfix-1587115620/1

class Solution:
    def precidence(self,op):
        if op=='+' or op=='-':
            return 1
        elif op =='*' or op=='/':
            return 2
        elif op =='^':
            return 3
        else:
            return -1
    def InfixtoPostfix(self, s):
        #code here
        
        ans = ""
        n = len(s)
        i =0
        stack = []
        while i<n:
            #If there is operand append it in answer
            if (s[i]>='A' and s[i]<='Z') or (s[i]>='a' and s[i]<='z') or (s[i]>='0' and s[i]<='9'):
                ans+=s[i]
            elif s[i]=='(':
                stack.append(s[i])
            elif s[i]==')':
                while stack and stack[-1]!='(':
                    ans+=stack.pop()
                stack.pop() #pop the ( character
            
            else: #operator
                char = s[i]
                while stack and self.precidence(char)<= self.precidence(stack[-1]):
                    ans+=stack.pop()
                stack.append(char)
            i+=1
        
        while stack:
            ans+=stack.pop()
        return ans