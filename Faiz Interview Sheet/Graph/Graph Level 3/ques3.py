#Question : Minimum Cost to Convert String I
#Link to the question:  https://leetcode.com/problems/minimum-cost-to-convert-string-i/

class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        n = len(original)
        MAXI = float('inf')
        dist = [[MAXI]*26 for _ in range(26)]

        #Diagonal element of dist =0
        for i in range(26):
            dist[i][i]=0

        #Prepopulate dist by min(cost,dist[][]),as dublicate is allowed so took the minimum value
        for i in range(n):
            org = ord(original[i])-ord('a')
            chan = ord(changed[i])-ord('a')
            dist[org][chan]= min(dist[org][chan],cost[i])
        
        #Flyod warshal algorithm
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k]!=MAXI and dist[k][j]!=MAXI:
                        dist[i][j]= min(dist[i][j],dist[i][k]+dist[k][j])
        
        #Iterate over the source and find the minimum cost
        ans =0
        for i in range(len(source)):
            s = ord(source[i])-ord('a')
            t = ord(target[i])-ord('a')
            if dist[s][t]==MAXI: #Indicates we cannt convert source to destination
                return -1
            ans += dist[s][t]
        
        return ans
