#Question : Trapping Rain Water
#Link to the question: https://leetcode.com/problems/trapping-rain-water/description/

#Method 1 : Using prefix and suffix array

class Solution(object):
    def trap(self, height):
        n = len(height)
        prefix=[0]*n
        suffix =[0]*n
        prefix[0]=height[0] 
        suffix[n-1]=height[n-1]
        for i in range(1,n):
            prefix[i]=max(height[i],prefix[i-1])
        for i in range(n-2,-1,-1):
            suffix[i]= max(suffix[i+1],height[i])
        ans =0
        for i in range(n):
            leftMax = prefix[i]
            rightMax = suffix[i]
            ans +=min(leftMax,rightMax)-height[i]
        return ans      
    
#Method 2 : Using two pointer Approach
class Solution(object):
    def trap(self, height):
        n = len(height)
        lMax=rightMax=ans=0
        left,right=0,n-1
        for i in range(n):
            if height[left]<=height[right]:
                if lMax>height[left]:
                    ans+=lMax-height[left]
                else:
                    lMax=height[left]
                left+=1
            else:
                if rightMax>height[right]:
                    ans+=rightMax-height[right]
                else:
                    rightMax=height[right]
                right-=1
        return ans


