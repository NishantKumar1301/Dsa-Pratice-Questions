#Question : Find Minimum Diameter After Merging Two Trees
#Link to the question: https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/description/?envType=daily-question&envId=2024-12-24

from collections import deque
class Solution(object):
    #Creation of the adjacency list
    def create_adj_list(self,edges,n):
        adj_list= [[] for _ in range(n)]
        for u ,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        return adj_list

    #Create a method to find total number of nodes on the given list of edges
    def count_node(self,edges):
        node = set()
        for u , v in edges:
            node.add(u)
            node.add(v)
            
        return len(node)

    #Create a bfs method
    def bfs(self,start,adj):
        visited =[False]*len(adj)
        queue = deque([start])
        visited[start]=True
        farthest_node = start
        diameter = -1
        while queue:
            length = len(queue)
            for _ in range(length):
                curr = queue.popleft()
                farthest_node = curr
                for neighbor in adj[curr]:
                    if not visited[neighbor]:
                        visited[neighbor]=True
                        queue.append(neighbor)
            diameter+=1
            
        return farthest_node,diameter

    #Create find diameter method
    """For finding the diameter follow the 3 steps : 
        1.> Select a random node possibly 0 th node 
        2.> Farthest node from the given random node will be the one end of the diameter
        3.> Farthest node from the one end of the diameter will be the second end of the diameter and the distance will be the diameter 
    """
    def find_diameter(self,edges):
        if not edges:
            return 0
        #Find the total number of nodes in the edges
        n = self.count_node(edges)
        adj =self.create_adj_list(edges,n)
        
        # Find the farthest node from an arbitrary start node
        start_node = 0
        farthest_node,_ = self.bfs(start_node,adj)#This is the first end of the diameter
        
        
        # Find the farthest node from the previously found farthest node to calculate the diameter
        second_end_of_diameter,diameter = self.bfs(farthest_node,adj)
        return diameter

    def minimumDiameterAfterMerge(self, edges1, edges2):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :rtype: int
        """
        # Calculate the diameters of the two trees
        diameter1 = self.find_diameter(edges1)
        diameter2 = self.find_diameter(edges2)

        # Calculate the radii of the two trees
        
        radius1 = (diameter1+1)//2
        radius2 = (diameter2+1)//2
        merged_diameter =1+radius1+radius2
        return max(merged_diameter,diameter1,diameter2)


