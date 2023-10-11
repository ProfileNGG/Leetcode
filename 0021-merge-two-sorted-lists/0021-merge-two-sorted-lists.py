# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2
        d = c = ListNode(0) #d와 c 초기화
        while list1 and list2: #두 리스트중 더 작은 숫자를 연결해줌
            if list1.val < list2.val: 
                c.next = list1
                list1 = list1.next
            else:
                c.next = list2
                list2 = list2.next
            c = c.next
        c.next = list1 or list2
        return d.next