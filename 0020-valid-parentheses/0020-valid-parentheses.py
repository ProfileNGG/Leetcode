class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(':')', '{':'}','[':']'}

        for c in s:
            if c in brackets:
                stack.append(c)
            elif stack and c == brackets[stack.pop()]:
                continue
            else:
                return False
        
        return not stack
