# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next # current next is saved to then be able to access the next element we need to reverse
            curr.next = prev # current next is changed to point to the previous (at the start null)
            # we update prev variable to be the current one, and current variable to be de next one
            prev = curr
            curr = nxt
        return prev

    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head:
    #         return None
        
    #     newHead = head
    #     if head.next:
    #         newHead = self.reverseList(head.next)
    #         head.next.next = head
    #     head.next = None

    #     return new_head