# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # using the dummy allows us to delete the head safely, without treating it as a special case
        left = dummy
        right = head
        
        # we shift the right pointer to be n pointers to the right of the start node
        while n > 0:
            right = right.next
            n -= 1
        # we move the pointers until right reaches None (the end of the linked list)
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next # we need to delete left.next, so we skip it by doing this
        return dummy.next