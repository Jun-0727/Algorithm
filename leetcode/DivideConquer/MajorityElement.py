from collections import Counter

def majorityElement(nums: list) -> int:
    counter = Counter(nums)

    for n in counter.keys():
        if counter[n] > (len(nums) // 2):
            return n
        

def divideConquer(nums: list) -> int:
    if not nums:
        return None
    
    if len(nums) == 1:
        return nums[0]
    
    mid = len(nums)//2
    a = divideConquer(nums[:mid])
    b = divideConquer(nums[mid:])

    if nums.count(a) > mid:
        return a
    else:
        return b
    

def pythony(nums: list) -> int:
    return sorted(nums)[len(nums)//2]

print(pythony([2,2,1,1,1,2,2]))