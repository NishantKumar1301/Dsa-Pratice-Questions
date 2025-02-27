#Question : Length of Longest Fibonacci Subsequence
#Link to the question: https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/?envType=daily-question&envId=2025-02-27

class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :r type: int
        """
        s= set(arr)
        ans = 0
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                prev,curr = arr[i],arr[j]
                nxt = prev + curr
                length = 2
                while nxt in s:
                    length+=1
                    prev,curr = curr,nxt
                    nxt = prev+curr
                    ans = max(ans,length)
        return ans
        

