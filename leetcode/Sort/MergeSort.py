def merge_sort(li: list) -> list:
    def merge(left: list, right: list) ->  list:
        merged = []

        while left and right:
            if left[0] <= right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
        
        if left:
            merged.extend(left)
        else:
            merged.extend(right)

        return merged
    
    if len(li) < 2:
        return li
    
    mid = len(li) // 2
    left = merge_sort(li[:mid])
    right = merge_sort(li[mid:])

    return merge(left, right)

print(merge_sort([1,5,2,6,2,4,5,6,2,4,4,6,9,6,2,4,11,44,6,2,3,5]))