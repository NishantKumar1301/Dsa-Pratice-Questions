#Question : Tree Boundary Traversal
#Link to the question:  https://www.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def isLeaf(self,root):
        if (not root.left) and (not root.right):
            return True
        else:
            return False

    def addLeftBoundary(self,root,ans):
        curr = root.left
        while curr:
            if not self.isLeaf(curr):
                ans.append(curr.data)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
    
    def addRightBoundary(self,root,ans):
        curr = root.right
        tmp = []
        while curr:
            if not self.isLeaf(curr):
                tmp.append(curr.data)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        for i in range(len(tmp)-1,-1,-1):
            ans.append(tmp[i])
    
    def addLeaf(self,root,ans):
        if self.isLeaf(root):
            ans.append(root.data)
            return
        if root.left:
            self.addLeaf(root.left,ans)
        if root.right:
            self.addLeaf(root.right,ans)
        
    def boundaryTraversal(self, root):
        # Code here
        
        ans = []
        if not root:
            return []
        if not self.isLeaf(root):
            ans.append(root.data)
        self.addLeftBoundary(root,ans)
        self.addLeaf(root,ans)
        self.addRightBoundary(root,ans)
        return ans