#Question : Find Elements in a Contaminated Binary Tree
#Link to the question: https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/description/?envType=daily-question&envId=2025-02-21

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements(object):
    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.node_set = set()
        if root:
            root.val = 0
            self.node_set.add(0)
            self.made_tree(root.left,1)
            self.made_tree(root.right,2)
    
    def made_tree(self,node,val):
        if not node :
            return 
        node.val = val
        self.node_set.add(val)
        self.made_tree(node.left,2*val+1)
        self.made_tree(node.right,2*val+2)

    def find(self, target):
        """
        :type target: int
        :r type: bool
        """
        return target in self.node_set
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

