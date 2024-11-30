#Question : Rotate the square matrix by 90 degree
#Link to the question: https://www.geeksforgeeks.org/problems/rotate-by-90-degree0356/1


def rotate(mat): 
    #code here
    m = len(mat)
    n = len(mat[0])
    for i in range(m):
        for j in range(i,n):
            mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
    for row in mat:
        row.reverse()
    return mat

