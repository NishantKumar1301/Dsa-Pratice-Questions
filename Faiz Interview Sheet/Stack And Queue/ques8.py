#Question : Trapping Rain Water
#Link to the question: https://leetcode.com/problems/trapping-rain-water/description/

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #Method 1
        # n = len(height)
        # ans = 0
        # prefix=[-1]*n
        # suffix = [-1]*n
        # prefix[0],suffix[n-1]=height[0],height[n-1]
        # for i in range(1,n):
        #     prefix[i]=max(prefix[i-1],height[i])
        # for i in range(n-2,-1,-1):
        #     suffix[i]= max(suffix[i+1],height[i])
        # for i in range(n):
        #     lmax = prefix[i]
        #     rmax = suffix[i]
        #     ans+=min(lmax,rmax)-height[i]
        # return ans 

        #Method 2 :
        n = len(height)
        lmax = rmax = ans = 0
        left,right = 0,n-1
        while left<right:
            if height[left]<=height[right]:
                if height[left]<lmax:
                    ans+=lmax-height[left]
                else:
                    lmax = height[left]
                left+=1
            else:
                if height[right]<rmax:
                    ans+=rmax-height[right]
                else:
                    rmax = height[right]
                right-=1
        return ans