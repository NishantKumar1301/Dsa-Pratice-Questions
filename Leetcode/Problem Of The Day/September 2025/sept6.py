#Question : Minimum Operations to Make Array Elements Zero
#Link to the question: https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/
class Solution(object):
    def solve(self,left,right):
        """
        L->R
        1-3 -> 1 step
        4-15 -> 2 step
        16-63 -> 3 step 
        if s tep then range = 4**(s-1) to 4**s-1
        """
        L = 1
        step =1
        cnt = 0
        while L<=right:
            R = 4*L-1
            start = max(left,L)
            end = min(right,R)
            if start<=end:
                cnt+=(end-start+1)*step
            L = 4*L
            step+=1
        return cnt


    def minOperations(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: int
        """
        ans =0
        for query in queries:
            left,right = query[0],query[1]
            ans+=(self.solve(left,right)+1)//2
        return ans