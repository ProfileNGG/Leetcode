class Solution:
    def strStr(self, h: str, n: str) -> int:
        l1,l2=len(h),len(n)
        for i in range(l1-l2+1):
            for j in range(l2):
                if n[j]!=h[i+j]:
                    break
                if j==l2-1:
                    return i
        return -1
