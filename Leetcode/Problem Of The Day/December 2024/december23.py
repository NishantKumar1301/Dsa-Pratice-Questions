#Question : Minimum Number of Operations to Sort a Binary Tree by Level
#Link to the question: https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/description/?envType=daily-question&envId=2024-12-23

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def count_swap(self,arr):
        sorted_arr = sorted(arr)
        n = len(arr)
        freq ={}
        ans =0
        for idx,value in enumerate(arr):
            freq[value]=idx
        
        for i in range(n):
            if arr[i]==sorted_arr[i]:
                continue
            
            correct_idx = freq[sorted_arr[i]]
            freq[arr[i]]=correct_idx
            freq[arr[correct_idx]]=i
            
            #swap ith index and correct index
            arr[i],arr[correct_idx]=arr[correct_idx],arr[i]
            ans+=1
        
        return ans

    def minimumOperations(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        queue = deque([root])
        ans =0
        while queue:
            length = len(queue)
            arr =[]
            for i in range(length):
                curr = queue.popleft()
                arr.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            ans +=self.count_swap(arr)
        return ans
        


