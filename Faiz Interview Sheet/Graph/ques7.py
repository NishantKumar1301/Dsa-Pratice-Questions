#Question : Clone Graph
#Link to the question: https://leetcode.com/problems/clone-graph/description/

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def dfs(self,node,cloned_node,map):
        for ngbr in node.neighbors:
            if ngbr not in map:
                cloned_ngbr = Node(ngbr.val)
                map[ngbr]=cloned_ngbr
                cloned_node.neighbors.append(cloned_ngbr)
                self.dfs(ngbr,cloned_ngbr,map)
            else:
                cloned_node.neighbors.append(map[ngbr])

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None
        cloned_node = Node(node.val)
        map = {}
        map[node]=cloned_node
        self.dfs(node,cloned_node,map)
        return cloned_node
        
