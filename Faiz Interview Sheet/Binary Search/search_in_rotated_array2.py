#Question : Search in Rotated Sorted Array II
#Link to the question: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums)
        low,high =0,n-1
        while low<=high:
            mid = low+(high-low)//2
            if nums[mid]==target:
                return True
            #Special Edge case : Not able to identify whether the left or the right half is sorted
            if nums[low]==nums[mid] and nums[mid]==nums[high]:
                low +=1
                high-=1
                continue
            #Left part is sorted
            if nums[low]<=nums[mid]:
                if nums[low]<=target<=nums[mid]:
                    high = mid -1
                else:
                    low = mid+1
            else:
                if nums[mid]<=target<=nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return False