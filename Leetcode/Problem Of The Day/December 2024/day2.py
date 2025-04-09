#Question : Find Champion II
#Link to the question: https://leetcode.com/problems/find-champion-ii/?envType=daily-question&envId=2024-11-26

class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        arr =[0]*n
        for edge in edges:
            arr[edge[1]]+=1
        count =0
        ans =-1
        for i in range(n):
            if arr[i]==0:
                count+=1
                ans = i
        # if count==1:
        #     return ans
        # else:
        #     return -1
        return ans if count ==1 else -1
        

