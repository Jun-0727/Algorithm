def twoSum(nums: list, target: int) -> list:
    result = []

    for i in range(len(nums)):
        if nums[i] < target:
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    result.append([i+1,j+1])
                
                if nums[i]+nums[j] > target:
                    break

    return result

print(twoSum([2,7,11,15], 9))
                
