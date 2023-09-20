class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s = s.split(' ') #공백을 기준으로 나눠주는 함수(함수 사용은 금지라 하셔서 지웠습니다)
        pattern = list(pattern) #모든 문자열을 나눠주는 함수(함수 사용은 금지라 하셔서 지웠습니다)

        if not len(s) == len(pattern): #패턴과 s의 길이가 다르면 거짓을 반환
            return False

        a = [None] * len(pattern) #패턴과 같은길이의 배열 생성
        b = [None] * len(s) #에스와 같은 길이의 배열 생성
        num = 0
        num1 = 0
        num2 = 0
        num3 = 0
        print(len(s))
        for i in range(0,len(pattern)): #배열의 모든 알파벳을 중복없이 a로 이동
            if a[i] == None:
                for j in range(0,len(a)):
                    if a[j] == pattern[i]:
                        num = 1
                if not num == 1:
                    a[num1] = pattern[i]
                    num = 0
                    num1 = num1 +1
                num = 0
        print(a)
        for i in range(0,len(s)): #배열의 모든 단어를 중복없이 b로 이동
            if b[i] == None:
                for j in range(0,len(b)):
                    if b[j] == s[i]:
                        num2 = 1
                if not num2 == 1:
                    b[num3] = s[i]
                    num2 = 0
                    num3 = num3 +1
                num2 = 0
        print(b)
        for k in range(0,len(a)): #a와 비교해서 패턴의 값을 숫자로 바꿈
            for k2 in range(0,len(pattern)):
                if a[k] == pattern[k2]:
                    pattern[k2] = k
        for k in range(0,len(b)):#b와 비교해서 에스의 값을 숫자로 바꿈
            for k2 in range(0,len(s)):
                if b[k] == s[k2]:
                    s[k2] = k
        for l in range(0,len(s)):#패턴과 s비교
            if not s[l] == pattern[l]:
                return False

        return True # 다 통과시 트루