#Question : Lexicographically Smallest Equivalent String
#Link to the question: https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/
from collections import defaultdict
class Solution(object):
    def dfs(self,char,visited,adj):
        visited[ord(char)-ord('a')]=True
        mini =  char
        for node in adj[char]:
            if not visited[ord(node)-ord('a')]:
                mini = min(mini,self.dfs(node,visited,adj))
        return mini

    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        adj = defaultdict(list)
        for u,v in zip(s1,s2):
            adj[u].append(v)
            adj[v].append(u)
        ans =[]
        for char in baseStr:
            visited=[False]*26
            ans.append(self.dfs(char,visited,adj))
        return "".join(ans)        