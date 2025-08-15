#Question : Binary Search Tree Iterator
#Link to the question: https://leetcode.com/problems/binary-search-tree-iterator/

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left


    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        r = node.right
        while r:
            self.stack.append(r)
            r = r.left
        return node.val



    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack)!=0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()