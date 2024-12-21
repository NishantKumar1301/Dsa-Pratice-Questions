#Question : Maximum Number of K-Divisible Components
#Link to the question: https://leetcode.com/problems/maximum-number-of-k-divisible-components/?envType=daily-question&envId=2024-12-21


class Solution(object):
    def dfs(self,adj_list,k,values,count,curr,parent=-1):
        total_sum = values[curr]
        for neighbor in adj_list[curr]:
            if neighbor != parent:
                total_sum+=self.dfs(adj_list,k,values,count,neighbor,curr)
        total_sum %=k
        if total_sum ==0:
            count[0]+=1
        return total_sum
        
    def maxKDivisibleComponents(self, n, edges, values, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type values: List[int]
        :type k: int
        """
        adj_list =[[] for _ in range(n)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        count =[0]
        self.dfs(adj_list,k,values,count,0)
        return count