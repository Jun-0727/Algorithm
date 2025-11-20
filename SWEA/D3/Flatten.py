## [SWEA / 1208번] Flatten ##

def flatten(box: list, count: int) -> int:
    
    for _ in range(count):
        top = max(box)          # 가장 높은 박스
        bottom = min(box)       # 가장 낮은 박스
    
        if top - bottom <= 1:   # 차이가 1이하 이면 종료
            return top - bottom

        # -- dump -- #
        hi = box.index(top)     # 가장 높은 박스의 위치
        lo = box.index(bottom)  # 가장 낮은 박스의 위치

        box[hi] -= 1
        box[lo] += 1
    
    return max(box) - min(box)

for t in range(1, 11):
    n = int(input())                        # dump 횟수 
    box = list(map(int, input().split()))   # 상자 초기화

    print(f'#{t} {flatten(box, n)}')