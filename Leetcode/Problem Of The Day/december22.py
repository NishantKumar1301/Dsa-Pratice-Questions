#Question : Find Building Where Alice and Bob Can Meet
#Link to the question:  https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/description/?envType=daily-question&envId=2024-12-22


class Solution(object):
    def __init__(self):
        self.seg_tree =[]
        
    def build_segTree(self,idx,left,right,arr):
        if left == right:
            self.seg_tree[idx] = left
            return 
        mid = left+(right-left)//2
        self.build_segTree(2*idx,left,mid,arr)
        self.build_segTree(2*idx+1,mid+1,right,arr)
        self.seg_tree[idx]=(self.seg_tree[2*idx] if arr[self.seg_tree[2*idx]]>arr[self.seg_tree[2*idx+1]] else self.seg_tree[2*idx+1])

    def rangeMaxQuery(self,start,end,left,right,arr,idx=1):
        if left>end or right<start: #NO OVERLAP
            return float('-inf')
        if left>=start and right<=end:#FULL OVERLAP
            return self.seg_tree[idx]
        mid = left+(right-left)//2#PARTIAL OVERLAP
        left_max = self.rangeMaxQuery(start,end,left,mid,arr,2*idx)
        right_max = self.rangeMaxQuery(start,end,mid+1,right,arr,2*idx+1)
        if left_max==float('-inf'):
            return right_max
        if right_max==float('-inf'):
            return left_max
        return left_max if arr[left_max]>= arr[right_max] else right_max
    
    
    def leftmostBuildingQueries(self, arr, queries):
        """
        :type heights: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(arr)
        self.seg_tree=[0]*(4*n+1)
        #Root is at 1 , left is at 2*idx, right child is at 2*idx+1
        #Step1 : Build the segment tree
        self.build_segTree(1,0,n-1,arr)
        
        res = []
        #Assign alice as minimum and bob as maximum
        for query in queries:
            alice = min(query[0],query[1])
            bob = max(query[0],query[1])
            
            #If alice == bob and arr[bob]>arr[alice] then return the index of bob
            if alice == bob or arr[bob]>arr[alice]:
                res.append(bob)
                continue
            
            #ELse find the next maximum element than alice and find its index
            # Binary Search + RMQ (Range Max Query)=DO binary search from the next index of bob to the rest
            #Assign left = bob +1 , right = n-1 , ans = float('inf')
            left,right,next_maxIndex = bob+1,n-1,float('inf')
            while left<=right:
                mid = left+(right-left)//2
                idx = self.rangeMaxQuery(left,mid,0,n-1,arr,1)
                if arr[idx]>arr[alice]:
                    right = mid-1
                    next_maxIndex = min(next_maxIndex,idx)
                else:
                    left = mid+1
            res.append(-1 if next_maxIndex ==float('inf') else next_maxIndex )
            
        return res 
        