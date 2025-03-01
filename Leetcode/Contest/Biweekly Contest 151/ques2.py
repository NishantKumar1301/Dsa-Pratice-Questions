#Question : Find the Number of Copy Arrays
#Link to the question: https://leetcode.com/contest/biweekly-contest-151/problems/find-the-number-of-copy-arrays/description/?slug=transform-array-by-parity&region=global_v2

class Solution(object):
    def countArrays(self, original, bounds):
        """
        :type original: List[int]
        :type bounds: List[List[int]]
        :r type: int
        """
        n = len(original)
        copy = [0]*n
        for i in range(n):
            copy[i]=original[i]-original[0]

        low = bounds[0][0]-copy[0]
        high = bounds[0][1]-copy[0]
        for i in range(1,n):
            low = max(low,bounds[i][0]-copy[i])
            high = min(high,bounds[i][1]-copy[i])
            if low > high:
                return 0
        return max(0,high-low+1)
        

