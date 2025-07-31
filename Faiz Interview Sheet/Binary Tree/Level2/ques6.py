#Question : Serialize and Deserialize Binary Tree
#Link to the question: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        ans = ""
        queue = deque([root])
        while  queue:
            curr = queue.popleft()
            if not curr:
                ans += "#,"
            else:
                ans+=str(curr.val)+","
                queue.append(curr.left)
                queue.append(curr.right)
        print(ans)
        return ans
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodes = data.split(",")
        root_val = nodes.pop(0)
        root = TreeNode(root_val)
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            left_val = nodes.pop(0)
            if left_val!="#":
                left_node = TreeNode(int(left_val))
                curr.left = left_node
                queue.append(curr.left)
            right_val = nodes.pop(0)
            if right_val!="#":
                right_node = TreeNode(int(right_val))
                curr.right= right_node
                queue.append(curr.right)
        return root
        

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))