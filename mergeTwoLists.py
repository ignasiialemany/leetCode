# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not l1: return l2
        if not l2: return l1

        # Create list
        if l1.val <= l2.val:
            answer = ListNode(l1.val, None)
            l1 = l1.next
        else:
            answer = ListNode(l2.val, None)
            l2 = l2.next

        # Create pointer to iterate along list
        iterator = answer

        # Keep merging lists based on comparison between values
        while (l1 != None and l2 != None):
            if l1.val <= l2.val:
                iterator.next = l1
                l1 = l1.next
            else:
                iterator.next = l2
                l2 = l2.next
            iterator = iterator.next

        # If any of the lists has not finished
        if (l1 != None):
            iterator.next = l1
        if (l2 != None):
            iterator.next = l2

        return answer