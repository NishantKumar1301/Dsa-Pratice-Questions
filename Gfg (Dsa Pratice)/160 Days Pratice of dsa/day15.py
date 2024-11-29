#Question : Implement Atoi
#Link to the question: https://www.geeksforgeeks.org/problems/implement-atoi/1

class Solution:
    def myAtoi(self, s):
        # Code here
        INT_MAX=2**31-1
        INT_MIN = -2**31
        ans =0
        sign = 1
        #Step1:Remove the leading white spaces : i>Use strip function
        ind=0
        while(ind<len(s) and s[ind]==" "):
            ind+=1
        s=s[ind:]
        
        if not s :
            return 0
        
        #Step3: Find the sign 
        if s[0]=="-":
            sign =-1
            s=s[1:]
        elif s[0]=="+":
            s=s[1:]
        
        #Step3:Loop through the string
        for char in s:
            if char.isdigit():
                ans = 10*ans+int(char)
                if sign == 1 and ans >=INT_MAX:
                    return INT_MAX
                if sign ==-1 and -1 *ans<= INT_MIN:
                    return INT_MIN
            else:
                break
        
        #Step4: Find the final ans
        ans = ans*sign
        return ans
            

