#Question : Convert Binary Number in a Linked List to Integer
#Link to the question: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        ans = 0
        while head:
            ans = (ans << 1) | head.val
            head = head.next
        return ans
        