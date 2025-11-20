## [SWEA / 1928번] Base64 Decoder ##

## 아스키 코드 조작 ##
# chr(): 아스키코드를 문자로 변환
# ord(): 문자를 아스키코드로 변환

## 2/8/10/16 진수 조작 ##
# 2진수: b / 8진수: o / 16진수: h

# format(int, '#b'): int를 2진수로 변환
# format(12, '#b') >> 0b1100

# format(int, 'b'): int를 2진수로 변환
# format(12, 'b') >> 1100

# format(int, '08b'): int를 6자리 2진수로 변환 & 앞자리는 0으로 초기화
# format(12, 'b') >> 00001100

# int(str, 2): 2진수를 10진수로 변환 
# int('1100', 2) >> 12
# int('1100', 8) >> 576(512+64)


encoding_table = {}     # 인코딩 테이블

# -- 인코딩 테이블 세팅 : 대문자 -- #
for ch in range(65,91):
    encoding_table[chr(ch)] = ch-65

# -- 인코딩 테이블 세팅 : 소문자 -- #
for ch in range(97,123):
    encoding_table[chr(ch)] = ch-71

# -- 인코딩 테이블 세팅 : 숫자 -- #
for ch in range(48,58):
    encoding_table[chr(ch)] = ch+4

# -- 인코딩 테이블 세팅 : 기호 -- #
encoding_table['+'] = 62
encoding_table['/'] = 63

def decode(encode_string: str) -> str:
    # -- 인코딩 문자 값을 2진수로 변경 -- #
    buffer = ''                     # buffer: 인코딩된 문자열이 2진수로 저장된 값
    for ch in encode_string:
        buffer += format(encoding_table[ch], '06b')

    # -- 디코딩된 2진수를 8-bit씩 쪼개서 아스키코드 변환 -- #
    plain_text = ''
    for i in range(0, len(buffer), 8):
        plain_text += chr(int(buffer[i:i+8], 2))

    return plain_text

T = int(input())

for t in range(1, T+1):
    s = str(input())
    
    print(f'#{t} {decode(s)}')