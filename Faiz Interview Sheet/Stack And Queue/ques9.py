#Question : Sum of Subarray Minimums
#Link to the question: https://leetcode.com/problems/sum-of-subarray-minimums/
MOD = 10**9 +7
class Solution(object):
    def previousSmaller(self,arr):
        n = len(arr)
        stack = []
        pse = [-1]*n
        #Store the index of just left side smaller element
        for i in range(n):
            while len(stack)>0 and arr[stack[-1]]>=arr[i]:
                stack.pop()
            pse[i]=-1 if len(stack)==0 else stack[-1]
            stack.append(i)
        return pse
    
    def nextSmaller(self,arr):
        n = len(arr)
        nse = [0]*n
        stack = []
        for i in range(n-1,-1,-1):
            while len(stack)>0 and arr[stack[-1]]>arr[i]:
                stack.pop()
            nse[i]=n if len(stack)==0 else stack[-1]
            stack.append(i)
        return nse

    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        pse = self.previousSmaller(arr)
        nse = self.nextSmaller(arr)
        ans = 0
        for i in range(n):
            left = i - pse[i]
            right = nse[i]-i
            total = (left * right * arr[i]) % MOD
            ans = (ans+total)%MOD
            # ans+=(total)% MOD
        return ans
        