from collections import Counter

def topKFrequent(nums: list, k: int) -> list:
    answer = []
    freq = Counter(nums)
    
    for key in freq:
        if freq[key] >= k:
            answer.append(key)

    return answer
    
    # return list(zip(*Counter(nums).most_common(k)))[0]

#print(topKFrequent([1,1,1,2,2,3], 2))

#[(1,3), (2,2)]
#[((1,3),), ((2,2),)]
l1 = [1,2,3,4]
l2 = [5,6,7,8]
print(list(zip(l1, l2)))