"""
[직사각형 판별하기]

배열 moves는 drawer가 움직일 방향이 순서대로 담겨있다.
Moves의 원소에 따라 drawer가 이동할 때, drawer가 이동한 경로가 직사각형인지 아닌지 판별하는 함수 solution(moves)를 완성

Ex.1)  >^<v		 ->	 True
Ex.2)  >^<^<v>v	 ->	 True
Ex.3)  <^<^>>	 ->	 False
Ex.4)  <<<^^^>>	 ->	 False
"""

def solution(moves):
    x, y = 0, 0         # 좌표(x,y)
    path = [(0,0)]      # 이동경로
    
    if not moves:
        return False
    
    for d in moves:
        if d == '^':
            y += 1
        elif d == 'v':
            y -= 1
        elif d == '<':
            x -= 1
        else:
            x += 1
        
        path.append((x,y))                      # 이동경로 세팅
        
    if (x,y) != (0,0):                          # 원점으로 돌아오지 못한 경우
        return False

    path_x = [p[0] for p in path]               # x좌표 이동 경로
    path_y = [p[1] for p in path]               # y좌표 이동 경로

    min_x, max_x = min(path_x), max(path_x)     # x좌표 최소/최대
    min_y, max_y = min(path_y), max(path_y)     # y좌표 최소/최대
    
    for x,y in path:                            # 모든 경로(선분)에 대해 직사각형을 이루는지 확인
        if not (x == min_x or x == max_x or y == min_y or y == max_y):
            return False
    
    return True

"""

Problem
직사각형 판별: count 리스트
count[0] : ^ 방향 이동 횟수 / count[1] : v 방향 이동 횟수
count[2] : > 방향 이동 횟수 / count[3] : < 방향 이동 횟수

Solved
><^v 의 경우 직사각형이 아니지만 직사각형으로 판별
>> 이동경로 path 리스트 생성

"""