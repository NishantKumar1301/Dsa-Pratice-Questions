#Question : Row With Maximum Ones
#Link to the question: https://leetcode.com/problems/row-with-maximum-ones/
from bisect import bisect_left
class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        #This is taking more time complexity as it is unsorted
        # idx = -1
        # maxone = 0
        # n = len(mat)
        # for i in range(n):
        #     mat[i].sort()
        #     cntone = len(mat[i]) - bisect_left(mat[i],1)
        #     if cntone>maxone:
        #         maxone = cntone
        #         idx = i
        # if idx==-1:
        #     idx=0
        # return [idx,maxone]

        #Method 2 : Time complexity : O(m*n)
        idx , maxone = 0,0
        for i , row in enumerate(mat):
            one = sum(row)
            if one>maxone:
                maxone = one
                idx = i
        return [idx,maxone]
