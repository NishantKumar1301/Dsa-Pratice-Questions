#Question : Flood Fill
#Link to the question: https://leetcode.com/problems/flood-fill/
class Solution(object):
    def dfs(self,image,row,col,color,ini_color,dr,dc,ans):
        ans[row][col]=color
        n = len(image)
        m = len(image[0])
        for i in range(4):
            nr,nc = row+dr[i],col+dc[i]
            if nr>=0 and nc>=0 and nr<n and nc<m and image[nr][nc]==ini_color and ans[nr][nc]!=color:
                self.dfs(image,nr,nc,color,ini_color,dr,dc,ans)

    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        #Duplicate of the given graph
        ans =[row[:] for row in image]
        dr =[-1,0,1,0]
        dc = [0,1,0,-1]
        ini_color = image[sr][sc]
        self.dfs(image,sr,sc,color,ini_color,dr,dc,ans)
        return ans
        