class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, dummy = head, head
        if not head:
            return head
        while head:
            if head.val == prev.val:
                head = head.next
                prev.next = head
            else:
                head = head.next
                prev = prev.next 
        return dummy
                