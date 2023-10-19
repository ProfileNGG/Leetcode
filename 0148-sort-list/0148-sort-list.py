class Solution(object):
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #노드 비었거나 하나일때 그냥 반환해주기
        if not head or not head.next:
            return head

        # 피벗 값을 맨 앞에있는 값으로 선택
        temp3 = head
        temp4 = head
        num = 0
        while temp3:
            temp3 = temp3.next
            num = num + 1
        for i in range(num//2):
            temp4 = temp4.next
        pivot = temp4.val

        # 작은 값, 같은 값, 큰 값에 대한 세 개의 연결 리스트 생성
        small_head = small_tail = ListNode(0)
        same_head = same_tail = ListNode(0)
        big_head = big_tail = ListNode(0)

        temp = head
        #각각 리스트에 값에 따른 노드 추가
        while temp:

            if temp.val < pivot:
                small_tail.next = temp
                small_tail = small_tail.next

            elif temp.val == pivot:
                same_tail.next = temp
                same_tail = same_tail.next

            else:
                big_tail.next = temp
                big_tail = big_tail.next
            temp = temp.next

        # 리스트들을 끊어주는 작업(안하면 무한재귀 돌 수 있음)
        small_tail.next = None
        same_tail.next = None
        big_tail.next = None

        # 작은 값과 큰 값 부분 리스트를 재귀적으로 정렬
        sorted_small = self.sortList(small_head.next)
        sorted_big = self.sortList(big_head.next)

        # 정렬된 부분 리스트를 연결
        if not sorted_small: #작은리스트 비어있으면 스킵하기
            sorted_head = same_head.next
        else:
            sorted_head = sorted_small
            temp = sorted_small
            while temp.next:
                temp = temp.next
            temp.next = same_head.next

        temp = sorted_head
        while temp.next:
            temp = temp.next
        temp.next = sorted_big

        return sorted_head