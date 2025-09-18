def mergeIntervals(li: list):
    merged = []
    li.sort(key = lambda x : x[0])

    for x in li:
        if merged and x[0] < merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], x[1])
        else:
            merged.append(x)

    return merged

print(mergeIntervals([[1,3], [2,6], [8,10], [15,18]]))