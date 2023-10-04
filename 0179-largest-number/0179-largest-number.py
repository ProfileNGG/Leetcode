class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if all(num == 0 for num in nums): 
            return "0"

        nums = list(map(str, nums))
        result = []
        
        while nums:
            max_num = "0"  # 초기값 설정
            for num in nums:
                if num + max_num > max_num + num:
                    max_num = num
            
            result.append(max_num)
            nums.remove(max_num)
        
        return ''.join(result)