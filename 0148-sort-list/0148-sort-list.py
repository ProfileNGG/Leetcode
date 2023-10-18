class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head

        # 연결 리스트의 길이를 계산
        length = 0
        temp1 = head
        while temp1:
            length += 1
            temp1 = temp1.next

        # 퀵 정렬을 위해 머지 소트와 비슷한 접근 사용
        temp2 = ListNode(0)
        temp2.next = head
        step = 1

        while step < length:
            temp1 = temp2.next
            tail = temp2
            while temp1:
                left = temp1
                right = self.split(left, step)
                temp1 = self.split(right, step)
                tail = self.merge(left, right, tail)
            step *= 2

        return temp2.next

    def split(self, head, step):
        if not head:
            return None
        for i in range(1, step):
            if not head.next:
                break
            head = head.next
        right = head.next
        head.next = None
        return right

    def merge(self, left, right, head):
        temp1 = head
        while left and right:
            if left.val < right.val:
                temp1.next = left
                left = left.next
            else:
                temp1.next = right
                right = right.next
            temp1 = temp1.next
        temp1.next = left or right
        while temp1.next:
            temp1 = temp1.next
        return temp1
