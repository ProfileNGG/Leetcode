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

            left = merge_sort(left)
            right = merge_sort(right)

            return merge(left, right)

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

            result.extend(left[i:])
            result.extend(right[j:])
            return result

        sorted_intervals = merge_sort(intervals)
        
        merged = [sorted_intervals[0]]
        for i in range(1, len(sorted_intervals)):
            current_interval = sorted_intervals[i]
            last_merged = merged[-1]

            if current_interval[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], current_interval[1])
            else:
                merged.append(current_interval)

        return merged