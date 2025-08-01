#Question : Pascal's Triangle
#Link to the question: https://leetcode.com/problems/pascals-triangle/?
class Solution(object):
    def ncr(self,n,r): # optimal way 10c3 = 10*9*8//1*2*3 = 10//1*9//2*8//3
        ans = 1
        for j in range(r):
            ans = ans*(n-j)
            ans = ans //(j+1)
        return ans
    #print nth row
    def generate_nth_row(self,n):
        ans = []
        ans.append(1)
        cnt = 1
        for j in range(1,n):
            cnt = cnt*(n-j)
            cnt = cnt//j
            ans.append(cnt)
        return ans
            
    def generate(self, numRows):
        #Method1: Using Brute force Time complexity = n^3
        # ans = []
        # for row in range(numRows):
        #     tmp = []
        #     for col in range(row+1):
        #         num = self.ncr(row,col)
        #         tmp.append(num)
        #     ans.append(tmp)
        # return ans

        # Method 2 : Time Complexity = n ^2
        ans = []
        for row in range(1,numRows+1):
            ans.append(self.generate_nth_row(row))
        return ans
