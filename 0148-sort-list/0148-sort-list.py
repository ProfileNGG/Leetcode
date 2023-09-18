# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        if not head or not head.next: #리스트가 비어있으면 그대로 반환
            return head
        temp1 = head.next 
        temp2 = head
        while temp1 and temp1.next: #템프 1 이랑 2를 증가시키면서 중간부분 찾기
            temp1 = temp1.next.next
            temp2 = temp2.next
        first = temp2.next #first에 중간부분 할당
        temp2.next = None
        a = self.sortList(head) #재귀함수
        b = self.sortList(first)#a 와 b에  
        return self.merge(a, b)
        
        
    def merge(self, a, b):
        if not a or not b:
            return a or b
        d = c = ListNode(0) #d와 c 초기화
        while a and b: #두 리스트중 더 작은 숫자를 연결해줌
            if a.val < b.val: 
                c.next = a
                a = a.next
            else:
                c.next = b
                b = b.next
            c = c.next
        c.next = a or b
        return d.next