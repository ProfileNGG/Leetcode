class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # 병합 정렬을 위한 함수
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2 #여기서 미드가 2일때
            left = arr[:mid] # 0,1 
            right = arr[mid:] # 2,3

            left = merge_sort(left)  # 왼쪽 부분 리스트를 재귀적으로 정렬
            right = merge_sort(right)  # 오른쪽 부분 리스트를 재귀적으로 정렬

            return merge(left, right)  # 정렬된 부분 리스트를 병합

        # 병합 함수
        def merge(left, right):
            result = []
            i = j = 0

            while i < len(left) and j < len(right): # 배열의 첫번째 요소를 기준으로 모든 배열을 정렬함
                if left[i][0] < right[j][0]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])  # 남은 리스트를 추가
            result.extend(right[j:])  # 남은 리스트를 추가
            return result

        sorted_intervals = merge_sort(intervals)  # 병합 정렬로 구간을 정렬
        
        merged = [sorted_intervals[0]] #한번 더 감싸서 [[a,b]] 형태로 줌
        for i in range(1, len(sorted_intervals)):# 0이아닌 1부터 n 까지(처음에 0과 비교함)
            current_interval = sorted_intervals[i]
            last_merged = merged[-1] # 머지드 배열의 마지막 요소
            if current_interval[0] <= last_merged[1]:# 뒷배열의 앞요소가 앞배열의 뒷요소보다 작으면 
                last_merged[1] = max(last_merged[1], current_interval[1])  # 구간 병합
            else:
                merged.append(current_interval)  # 겹치지 않는 경우 새로운 배열 추가

        return merged  # 병합된 구간 리스트 반환