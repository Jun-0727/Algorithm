## [SWEA / 1859번] 백만 장자 프로젝트 ##

def get_max_profit(prices: list) -> int:
    max_price = max(prices[0:])                 # 구간별 최대 가격
    profit = 0                                  # 총 이익

    for i in range (len(prices)-1):
        if prices[i] < max_price:               # 현재 가격과 최대가격 비교 
            profit += (max_price - prices[i])   
        else:                                   # 구간별 최대 가격 초기화
            max_price = max(prices[i+1:])

    return profit

T = int(input())            # 테스트 케이스

for t in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    profit = get_max_profit(prices)
    
    print(f'#{t+1} {profit}')
