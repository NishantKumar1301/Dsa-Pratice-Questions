#Question : Delete Nodes From Linked List Present in Array
#Link to the question: https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums = set(nums)
        dummy = ListNode(next=head)
        cur = dummy
        while cur.next:
            if cur.next.val in nums:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next