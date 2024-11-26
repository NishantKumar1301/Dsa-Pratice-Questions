#Question : Maximum Matrix Sum
#Link to the question: https://leetcode.com/problems/maximum-matrix-sum/?envType=daily-question&envId=2024-11-26

#Observtion :
"""1>.If even number of negative sign are there then all the negative sign gets cancelled
    2.If there is odd number of negative sign then only one negative sign is left which is 
        attached with the minimum value"""

class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        total_sum=0
        min_val = float("inf")
        neg_count=0
        for i in range(n):
            for j in range(n):
                if matrix[i][j]<0:
                    neg_count+=1
                total_sum+=abs(matrix[i][j])
                min_val= min(min_val,abs(matrix[i][j]))
        if neg_count%2==0:
            return total_sum
        else:
            return total_sum-2*min_val