# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy # one node right before our group

        while True:
            kth = self.getKth(groupPrev, k) # last node in the group
            if not kth:
                break
            groupNext = kth.next #  first node after the current group

            #reverse group
            prev, curr = kth.next, groupPrev.next # curr is the first node in the current group
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = groupPrev.next # this is the old start of the group, 1
            groupPrev.next = kth # we put kth (in the example 3) at the beginning of the group, after the dummy
            groupPrev = tmp # now groupPrev is the end of the reversed group, it moves to the end of the reversed group, 1
        return dummy.next
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr