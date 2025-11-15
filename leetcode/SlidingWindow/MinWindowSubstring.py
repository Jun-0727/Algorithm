from collections import Counter

s = 'ADOBECODEBANC'
t = 'ABC'

def minWindow(s: str, t: str) -> str:
    start, end = 0, len(s)+1

    # N번 반복
    for ptr, char in enumerate(s):
        need = Counter(t)
        missing = len(t)

        # 왼쪽 포인터 초기화
        if char in t:
            left = ptr
            need[char] -= 1
            missing -= 1
            
            # 문자열T의 개수가 한 개인 경우
            if missing == 0:
                return t

            # 오른쪽 포인터 이동
            for right, char in enumerate(s[left+1:], left+1):
                if need[char] > 0:
                    need[char] -= 1
                    missing -= 1

                    # 모든 문자를 찾았으면 종료
                    if missing == 0:
                        # 앞에서 찾은 길이보다 짧은 길이의 문자열을 찾은 경우 start, end 초기화
                        if end-start > right-left:
                            start, end = left, right+1
                        break                


    # 문자열T의 모든 문자가 문자열S 포함되지 않는 경우
    if end - start > len(s):
        return ''
    
    return s[start:end]

print(minWindow(s, t))
