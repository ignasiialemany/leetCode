class Solution:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return None

        node = ListNode()
        answer = node

        duplicateValue = float("-inf")

        while (head.next != None):
            if head.val != head.next.val and head.val != duplicateValue:
                node.next = ListNode(val=head.val)
                node = node.next
                head = head.next
            else:
                duplicateValue = head.val
                head = head.next

        if head.val != duplicateValue:
            node.next = head

        return answer.next