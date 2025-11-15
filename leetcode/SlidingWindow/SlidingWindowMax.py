## BruteForce ##

# def maxSlidingWindow(self, nums: list, k: int) -> list:
#    if not nums:
#        return nums
#    
#    result = []
#    for i in range(len(nums)-k+1):
#        result.append(max(nums[i:i+k]))
#
#    return result

## Queue ##
from collections import deque

def maxSlidingWindow(nums: list, k: int) -> list:
    result = []
    max_num = 0
    window = deque()

    for idx, val in enumerate(nums):
        window.append(val)

        # 윈도우 초기 세팅
        if idx < k-1:
            max_num = max(window)
            continue
        
        # 새로운 원소 확인
        if max_num < val:
            max_num = val
        
        result.append(max_num)

        # 윈도우 범위 세팅
        if max_num == window.popleft():
            max_num = max(window)

    return result

nums = [1,3,-1,-3,5,3,6,7]

answer = maxSlidingWindow(nums, 3)
print(answer)