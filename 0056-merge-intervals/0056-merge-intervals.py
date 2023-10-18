class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # 병합 정렬을 위한 함수
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            left = merge_sort(left)  # 왼쪽 부분 리스트를 재귀적으로 정렬
            right = merge_sort(right)  # 오른쪽 부분 리스트를 재귀적으로 정렬

            return merge(left, right)  # 정렬된 부분 리스트를 병합

        # 병합 함수
        def merge(left, right):
            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i][0] < right[j][0]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])  # 남은 왼쪽 부분 리스트를 추가
            result.extend(right[j:])  # 남은 오른쪽 부분 리스트를 추가
            return result

        sorted_intervals = merge_sort(intervals)  # 병합 정렬로 구간을 정렬
        
        merged = [sorted_intervals[0]]
        for i in range(1, len(sorted_intervals)):
            current_interval = sorted_intervals[i]
            last_merged = merged[-1]

            if current_interval[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], current_interval[1])  # 구간 병합
            else:
                merged.append(current_interval)  # 겹치지 않는 경우 새로운 구간 추가

        return merged  # 병합된 구간 리스트 반환