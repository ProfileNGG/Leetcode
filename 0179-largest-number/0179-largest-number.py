class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 비교 함수를 정의합니다.
        def custom_compare(x, y):
            xy = str(x) + str(y)
            yx = str(y) + str(x)
            return (int(xy) > int(yx)) - (int(xy) < int(yx))
        
        # 비교 함수를 사용하여 숫자 리스트를 정렬합니다.
        nums.sort(key=functools.cmp_to_key(custom_compare), reverse=True)
        
        # 0으로만 이루어진 리스트인 경우 '0'을 반환합니다.
        if nums[0] == 0:
            return "0"
        
        # 정렬된 숫자를 문자열로 변환하여 반환합니다.
        result = "".join(map(str, nums))
        return result