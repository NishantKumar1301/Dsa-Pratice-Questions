#Question : Fruits Into Baskets III
#Link to the question: https://leetcode.com/problems/fruits-into-baskets-iii/
class Solution(object):
    def build_tree(self,idx,left,right,segment_tree,baskets):
        if left==right:
            segment_tree[idx]= baskets[left]
            return
        mid = left+(right-left)//2
        self.build_tree(2*idx+1,left,mid,segment_tree,baskets)
        self.build_tree(2*idx+2,mid+1,right,segment_tree,baskets)
        segment_tree[idx]= max(segment_tree[2*idx+1],segment_tree[2*idx+2])

    def query_segment_tree(self,idx,left,right,segment_tree,fruit):
        if fruit>segment_tree[idx]:
            return False
        if left==right:
            segment_tree[idx]=-1
            return True
        flag = False
        mid = left+(right-left)//2
        if segment_tree[2*idx+1]>=fruit:
            flag = self.query_segment_tree(2*idx+1,left,mid,segment_tree,fruit)
        else:
            flag = self.query_segment_tree(2*idx+2,mid+1,right,segment_tree,fruit)
        segment_tree[idx]= max(segment_tree[2*idx+1],segment_tree[2*idx+2])
        return flag

    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n = len(baskets)
        segment_tree =[-1]*(4*n)
        self.build_tree(0,0,n-1,segment_tree,baskets)
        cnt = 0
        for fruit in fruits:
            if not self.query_segment_tree(0,0,n-1,segment_tree,fruit):
                cnt+=1
        return cnt
        