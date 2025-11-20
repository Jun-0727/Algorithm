## 평범한 배낭 ## 

# 0-1 KnapSack Problem
# 가방에 넣을 수 있는 물건의 무게와  가치

# 1. 물건을 하나씩 꺼내서
# 2. 가방의 용량이 0 ~ n kg일 때
# 3. 물건을 가방에 넣을 수 있다면
# 4. 넣는게 이득인지 / 안 넣는게 이득인지

# 확인해가는 과정

loads = []
N, K = map(int, input().split())

def knapsack(loads: int, k: int) -> int:                # loads: 물건 리스트 / k: 가방 용량
    dp = [[] * (k+1) for _ in range(len(loads)+1)]

    for i in range(len(loads) + 1):                     # i: n번째 물건(1~n)
        for volume in range(k+1):                       # volume: 가방 용량
            weight = loads[i-1][0]                      # weight: 물건의 무게 / loads[i]가 아닌 loads[i-1]임에 주의
            value = loads[i-1][1]                       # value: 물건의 가치 / loads[i]가 아닌 loads[i-1]임에 주의
            
            if i == 0 or volume == 0:                   # 물건을 담지 않는 경우 / 가방 용량이 0 인 경우
                dp[i][volume] = 0
            
            elif weight > volume:                       # 물건을 가방에 넣을 수 있다면
                dp[i][volume] = max(
                    dp[i-1][volume],                    # 넣지 않았을 경우
                    value + dp[i-1][volume - weight]    # 넣었을 경우: 물건의 가치 + 물건을 담고 남은 무게 중, 다른 물건을 담을 수 있는 최대 가치
                    ) 
                
            else:                                       # 물건을 가방에 넣을 수 없다면
                dp[i][volume] = dp[i-1][volume]

    return dp[-1][-1]