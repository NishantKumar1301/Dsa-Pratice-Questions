#User function template for Python
#Question : Floyd Warshall
#Link to the question: https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1

class Solution:
    def floydWarshall(self, mat):
        #Code here
        n = len(mat)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if mat[i][k] != int(1e8) and mat[k][j] != int(1e8):
                        mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])

        #For negative cycle
        for i in range(n):
            if mat[i][i] < 0:
                return -1 
