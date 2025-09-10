def longestSubstring(string: str) -> int:
    used = {}
    max_length = 0
    start = 0
    
    for index, char in enumerate(string):
        if char in used and used[char] >= start:
            start = used[char] + 1
        
        max_length = max(max_length, index - start + 1)
        used[char] = index

    return max_length


print(longestSubstring('abccdfdgac'))