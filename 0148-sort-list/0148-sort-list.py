# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        temp = head.next
        temp2 = head
        while temp and temp.next:
            temp = temp.next.next
            temp2 = temp2.next
        piv = temp2.next
        left_h = left_t = ListNode(0)
        equal_h = equal_t = ListNode(0)
        right_h = right_t = ListNode(0)
        temp3 = head
        while temp3:
            if temp3.val < piv.val:
                left_t.next = temp3
                left_t = left_t.next
            elif temp3.val == piv.val:
                equal_t.next = temp3
                equal_t = equal_t.next
            else:
                right_t.next = temp3
                right_t = right_t.next
            temp3 = temp3.next
        left_t.next = None
        right_t.next = None
        equal_t.next = None

        right_h = self.sortList(right_h.next)
        left_h = self.sortList(left_h.next)
        
        
        if not left_h:
            sort_h = equal_h.next
        else:
            sort_h = left_h
            temp4 = sort_h
            while temp4.next:
                temp4 = temp4.next
            temp4.next = equal_h.next

        temp4 = sort_h
        while temp4.next:
            temp4 = temp4.next
        temp4.next = right_h
        
        return sort_h
            

                
                

    
            
