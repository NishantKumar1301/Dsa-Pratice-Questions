#Question : Keys and Rooms
#Link to the question: https://leetcode.com/problems/keys-and-rooms/description/

class Solution(object):
    def dfs(self,src,rooms,visited):
        visited[src]=True
        for room in rooms[src]:
            if not visited[room]:
                self.dfs(room,rooms,visited)
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        #Find total number of rooms
        n = len(rooms)
        visited = [False]*n
        #Make a dfs call from room 0 as source as it is opened always
        self.dfs(0,rooms,visited)
        #Traverse Through the visited if any of them is false that mean there is no path for that node 
        for node in visited :
            if node==False:
                return False
        return True
        
