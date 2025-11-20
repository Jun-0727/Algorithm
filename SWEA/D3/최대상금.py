## [SWEA / 1244번] 최대상금 ##

def swap_cards(prize: int) -> list:
    results = set()                                         # 카드 위치가 바뀐 모든 경우의 수(중복제거)

    cards = list(map(int, str(prize)))                      # 타입변환: int -> list
    
    for i in range(len(cards)):
        for j in range(i+1, len(cards)):
            tmp = cards[:]
            tmp[i], tmp[j] = tmp[j], tmp[i]                 # i번째 카드 & j번째 카드 swap
            results.add(int(''.join(str(x) for x in tmp)))  # 타입변환 list -> int
    
    return list(results)


def max_prize(prize: int, k: int) -> int:
    prizes = set()                      # 받을 수 있는 상금 후보
    nums = [prize]                      # 받을 수 상금 리스트

    for _ in range(k):                  # 교환 횟수
        prizes.clear()                  # 상금 후보 초기화(새로운 상금 후보를 담아야 함)
        for num in nums:                # num: prize(상금)
            for x in swap_cards(num):
                prizes.add(x)

        nums = list(prizes)             # 받을 수 있는 상금 후보 set -> list
    
    return max(prizes)


T = int(input())

for t in range(1, T+1):
    cards, count = map(int, input().split())
    print(f'#{t} {max_prize(cards, count)}')

    