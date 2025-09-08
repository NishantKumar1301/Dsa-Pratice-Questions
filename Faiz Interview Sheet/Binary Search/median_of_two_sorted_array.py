#Question : Median of Two Sorted Arrays
#Link to the question: https://leetcode.com/problems/median-of-two-sorted-arrays/
#Time complexity : O(log2(min(n1,n2)))

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        #Apply binary search on the smallest array to reduce the time complexity
        n1,n2 = len(nums1),len(nums2)
        n = n1+n2
        left = (n1+n2+1)//2 # length of left half
        if n1>n2:
            return self.findMedianSortedArrays(nums2,nums1)
        low = 0 
        high = n1
        while low<=high:
            mid1 = low+(high-low)//2
            mid2 = left -mid1
            l1,l2,r1,r2 = float('-inf'),float('-inf'),float('inf'),float('inf')
            if mid1<n1:
                r1 = nums1[mid1]
            if mid2<n2:
                r2 = nums2[mid2]
            if mid1-1>=0:
                l1 = nums1[mid1-1]
            if mid2-1>=0:
                l2 = nums2[mid2-1]
            
            #Apply the condition : l1<=r1 and l2<=r1 , then only valid
            if l1<=r2 and l2<=r1:
                #If odd then return max(l1,l2)
                if n%2==1:
                    return max(l1,l2)
                else:
                    #Return (left+right)/2.0
                    left = max(l1,l2)
                    right = min(r1,r2)
                    ans = (float(left) + float(right))/2.0
                    return ans
            #If l1>r2 then eliminate right half , high = mid-1
            elif l1>r2:
                high = mid1-1
            else:
                low = mid1+1
        return 0