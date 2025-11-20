## [SWEA / 25655번] 유치원생은 쉽게 푸는 문제 ##

def minNum(x: int) -> int:
    if x == 0:
        return 1
    
    if x == 1:
        return 0
    
    if x%2 == 0:
        return '8'* (x//2)

    if x%2 == 1:
        return '4' + '8' * ((x-1)//2)
    

T = int(input())

for t in range(T):
    print(minNum(int(input())))