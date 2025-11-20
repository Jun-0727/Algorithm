## [SWEA / 1284] 수도 요금 경쟁 ##

# P: 회사A 리터당 비용
# Q: 회사B 기본 요금 / R: 회사B 요금 부과 기준 / S: 회사B 리터당 비용
# W: 사용량

def water_bill(P, Q, R, S, W):  
    if W <= R:
        return min(W*P, Q)
    else:
        return min(W*P, Q+((W-R)*S))
    
T = int(input())

for t in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    print(f'#{t} {water_bill(P, Q, R, S, W)}')