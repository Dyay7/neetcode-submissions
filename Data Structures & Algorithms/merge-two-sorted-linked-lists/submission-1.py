# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        dummy = node = ListNode() # node will move forward, we use dummy to return the head later

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 or list2 # when one list becomes empty we attack the remaining nodes of the other list to node.next

        return dummy.next # dummy.next is the head of the linked list, since dummy doesn't hold a val, only
        # the reference to the head

    
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     if list1 is None:
    #         return list2
    #     if list2 is None:
    #         return list1
    #     if list1.val <= list2.val:
    #         list1.next = self.mergeTwoLists(list1.next, list2) # Each return gives the caller the head of the merged list so far.
    #         return list1
    #     else:
    #         list2.next = self.mergeTwoLists(list1, list2.next)
    #         return list2