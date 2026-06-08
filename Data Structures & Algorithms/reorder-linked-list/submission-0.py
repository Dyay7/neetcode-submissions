# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is at the end of the first half
        second = slow.next
        slow.next = None  # split the list

        # reverse the second half
        prev, curr = None, second
        while curr:
            nxt = curr.next      # save next node
            curr.next = prev     # reverse pointer
            prev = curr          # move prev forward
            curr = nxt           # move curr forward

        second = prev  # new head of reversed second half

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2