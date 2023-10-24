class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """docstring""" 
        num2_index = 0
        for index in range(m, m + n):
            nums1[index] = nums2[num2_index]
            num2_index += 1
        for starter in range(0, m + n):
            for position in range(starter + 1, m + n):
                if nums1[starter] > nums1[position]:
                    nums1[starter], nums1[position] = nums1[position], nums1[starter]