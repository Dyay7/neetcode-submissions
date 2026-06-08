# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_pointer = head
        fast_pointer = head
        # slow pointer moves 1 at a time and fast pointer moves 2 at a time
        # if there is a cycle, fast pointer will eventually be equal to slow pointer
        # if not, fast_pointer will end up reaching null so the loop stops
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False


