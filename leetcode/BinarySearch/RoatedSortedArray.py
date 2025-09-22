def roatedSortedArray(nums: list, target: int):
    pivot = nums.index(min(nums))

    if nums[0] <= target and target <= nums[pivot-1]:
        left, right = 0, pivot-1
    else:
        left, right = pivot, len(nums) - 1
    

    while left <= right:
        mid = left + ((right - left) // 2)

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid

    return -1

print(roatedSortedArray([3,4,5,0,1,2], 2))

