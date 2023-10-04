class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if all(num == 0 for num in nums): #0이면 0을 반환
            return "0"

        nums = list(map(str, nums)) #리스트를 문자열로 변환
        result = []
        
        while nums:
            maxnum = "0"  # 초기값 설정
            for num in nums:
                if num + maxnum > maxnum + num:
                    maxnum = num
            
            result.append(maxnum)
            nums.remove(maxnum)
        
        return ''.join(result)