#Question : Maximize the Number of Target Nodes After Connecting Trees I
#Link to the question: https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/?envType=daily-question&envId=2025-05-28

class Solution:
    def maxTargetNodes(self,edges1, edges2, k):
        def dfs(node, parent, children, k):
            if k < 0:
                return 0
            res = 1
            for child in children[node]:
                if child == parent:
                    continue
                res += dfs(child, node, children, k - 1)
            return res

        def build(edges, k):
            n = len(edges) + 1
            children = [[] for _ in range(n)]
            for u, v in edges:
                children[u].append(v)
                children[v].append(u)
            res = [0] * n
            for i in range(n):
                res[i] = dfs(i, -1, children, k)
            return res

        n = len(edges1) + 1
        count1 = build(edges1, k)
        count2 = build(edges2, k - 1)
        maxCount2 = max(count2)
        res = [count1[i] + maxCount2 for i in range(n)]
        return res