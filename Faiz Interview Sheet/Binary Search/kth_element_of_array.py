#Question : K-th element of two Array
#Link to the question: https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1
class Solution:
    def kthElement(self, a, b, k):
        # code here
        m,n = len(a),len(b)
        if m>n:
            return self.kthElement(b,a,k)
        left = k
        low = max(0,k-n)
        high = min(m,k)
        while low<=high:
            mid1 = low +(high-low)//2
            mid2 = left -mid1
            l1,l2,r1,r2 = float('-inf'),float('-inf'),float('inf'),float('inf')
            if mid1<m:
                r1 = a[mid1]
            if mid2<n:
                r2 = b[mid2]
            if mid1-1>=0:
                l1 = a[mid1-1]
            if mid2-1>=0:
                l2 = b[mid2-1]
            if l1<=r2 and l2<=r1:
                return max(l1,l2)
            elif l1>r2:
                high = mid1-1
            else:
                low = mid1+1
        return 0