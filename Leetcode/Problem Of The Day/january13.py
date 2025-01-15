#Question : Find the Prefix Common Array of Two Arrays
#Link to the question: https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/


class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)
        freq = [0]*(n+1)
        ans = [0]*n
        count = 0
        for i in range(n):
            freq[A[i]]+=1
            if freq[A[i]]==2:
                count +=1
            freq[B[i]]+=1
            if freq[B[i]]==2:
                count+=1
            ans[i]=count
        return ans
        
        