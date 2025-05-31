#Question : Snakes and Ladders
#Link to the question: https://leetcode.com/problems/snakes-and-ladders/?envType=daily-question&envId=2025-05-31
from collections import deque
class Solution(object):
    def get_cordinate(self,num,n):
        row_from_top = (num-1)//n
        row_from_bottom  = (n-1)-row_from_top #n-1 bcoz it is is 1 based indexing
        col = (num-1)%n
        #If both n and row_from_bottom are of same parity then right ->left movement so col = n-1-col
        if((n%2==1 and row_from_bottom%2==1) or (n%2==0 and row_from_bottom %2==0)):
            col = (n-1)-col
        return row_from_bottom, col

    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        queue = deque()
        queue.append(1)
        visited =[[False]*n for _ in range(n)]
        visited[n-1][0]=True
        ans = 0
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr==n*n:
                    return ans
                for k in range(1,7):
                    next_pos = curr+k
                    if next_pos>n*n:
                        break
                    row,col = self.get_cordinate(next_pos,n)
                    if not visited[row][col]:
                        visited[row][col]=True
                        if board[row][col]==-1:
                            queue.append(next_pos)
                        else:
                            queue.append(board[row][col])
            ans+=1
        return -1
