#Question : Candy
#Link to the question:https://leetcode.com/problems/candy/?envType=daily-question&envId=2025-06-02
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        left=[0]*n
        right= [0]*n
        left[0]=right[n-1]=1
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                left[i]=left[i-1]+1
            else:
                left[i]=1
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                right[i]=right[i+1]+1
            else:
                right[i]=1
        ans = 0
        for i in range(n):
            ans += max(left[i],right[i])
        return ans
        