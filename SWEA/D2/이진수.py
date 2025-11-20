## [SWEA / 5185번] 이진수 ##

def hex2bin(s: str) -> str:
    answer = ''

    for ch in s:
        num = int(ch, 16)           # hex -> int
        bin = format(num, '04b')    # int -> bin
        answer += bin
    
    return answer

T = int(input())

for t in range(1,T+1):
    n, s = map(str, input().split())
    print(f'#{t} {hex2bin(s)}')