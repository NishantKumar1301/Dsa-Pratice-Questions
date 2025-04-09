#Question :Range Sum Query - Mutable
#Link to the question: https://leetcode.com/problems/range-sum-query-mutable/description/

class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.segment_tree = [0] * (4 * self.n)
        self.build_segment_tree(0, 0, self.n - 1, nums)

    def build_segment_tree(self, i, l, r, nums):
        if l == r:
            self.segment_tree[i] = nums[l]
            return
        mid = l + (r - l) // 2
        self.build_segment_tree(2 * i + 1, l, mid, nums)
        self.build_segment_tree(2 * i + 2, mid + 1, r, nums)
        self.segment_tree[i] = self.segment_tree[2 * i + 1] + self.segment_tree[2 * i + 2]

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.update_seg_tree(index, val, 0, 0, self.n - 1)

    def update_seg_tree(self, index, val, i, l, r):
        if l ==r:
            self.segment_tree[i]=val
            return
        mid = l+(r-l)//2
        if index<=mid:
            self.update_seg_tree(index,val,2*i+1,l,mid)
        else:
            self.update_seg_tree(index,val,2*i+2,mid+1,r)
            
        self.segment_tree[i]=self.segment_tree[2*i+1]+self.segment_tree
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.query_segment_tree(left, right, 0, 0, self.n - 1)

    def query_segment_tree(self, start, end, i, l, r):
        if l > end or r < start:
            return 0
        if l >= start and r <= end:
            return self.segment_tree[i]
        mid = l + (r - l) // 2
        return self.query_segment_tree(start, end, 2 * i + 1, l, mid) + \
               self.query_segment_tree(start, end, 2 * i + 2, mid + 1, r)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)