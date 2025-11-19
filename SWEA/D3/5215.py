## 햄버거 다이어트 ##

# 0-1 KnapSack Problem
# 버거에 넣을 수 있는 재료의 칼로리와 맛

# 1. 재료를 하나씩 확인하면서
# 2. 먹을 수 있는 칼로리 총량이 0 ~ n cal일 때
# 3. 재료의 칼로리가 오늘 먹어도 되는 칼로리 총량 보다 작을 때
# 4. 넣는게 이득인지 / 안 넣는게 이득인지
# 확인해가는 과정


def max_flavor_score(foods: list, limits: int) -> int:
    dp = [[0] * (limits+1) for _ in range(len(foods)+1)]        # dp 초기화

    for i in range(len(foods) + 1):                             # i: n번째 재료 
        for limit in range(limits+1):                           # limit: 최대로 먹을 수 있는 칼로리
            flavor, cal = foods[i-1][0], foods[i-1][1]          # flavor: 맛 점수 / cal: 칼로리
            
            if i == 0 or limit == 0:                            # i = 0: 넣는 재료 X / limit = 0: 먹을 수 있는 칼로리 0
                dp[i][limit] = 0
            
            elif cal < limit:                                   # 재료의 칼로리 < 최대로 먹을 수 있는 칼로리
                dp[i][limit] = max(dp[i-1][limit], flavor + dp[i-1][limit - cal])
            
            else:
                dp[i][limit] = dp[i-1][limit]

    return dp[-1][-1]

T = int(input())

for t in range (1, T+1):
    N, L = map(int, input().split())

    flavors = []
    for _ in range(N):
        flavors.append(list(map(int, input().split())))

    print(f'#{t} {max_flavor_score(flavors, L)}')

