"""
[String 처리하기]
주어진 문자열에 대해서 연속하는 문자열이 3개 이상이 넘어가지 않도록 처리하는 함수 solution(S)를 완성

Ex.1)  aaabc 		-> 	aabc
Ex.2)  aaabbbccc	->	aabbcc
Ex.3)  xxxxuuxxxx	-> 	xxuuxx
"""

def solution(S):
    if len(S) < 3:
        return S
    
    answer = []
    for ch in S:
        if len(answer) >= 2 and answer[-1] == ch and answer[-2] == ch:
            continue
        answer.append(ch)
    
    return ''.join(answer)

