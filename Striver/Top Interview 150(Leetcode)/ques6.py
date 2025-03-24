#Question : Rotate Array
#Link to the question: https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150


class Solution(object):
    def helper(self,arr,start,end):
        while start<=end:
            temp = arr[start]
            arr[start]=arr[end]
            arr[end]=temp
            start+=1
            end-=1
        
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        self.helper(nums,0,n-1)
        self.helper(nums,0,k-1)
        self.helper(nums,k,n-1)
        return nums

