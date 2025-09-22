def intersection(nums1: list, nums2: list):
    result = set()
    for x in nums1:
        if not x in result and x in nums2:
            result.add(x)

    return list(result)

print(intersection([4,9,5], [9,4,9,8,4]))