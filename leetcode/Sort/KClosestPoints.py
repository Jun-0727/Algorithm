from heapq import heappush, heappop

points = [[1,3],[-2,2]]
K = 1

def k_closest_points(points: list, K: int) -> list:
    nums = []    
    for x, y in points:
        dist = pow(x,2) + pow(y,2)
        heappush(nums, (dist, x, y))

    result = []
    for i in range(K):
        p, x, y = heappop(nums)
        result.append([x,y])
        
    return result

print(k_closest_points(points, K))
