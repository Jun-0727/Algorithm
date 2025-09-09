def isValid(s: str) -> bool:
    stack = []
    table = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char not in table:
            stack.append(char)
        else:
            if not stack or stack.pop() != table[char]:
                return False
            
    if stack:
        return False
    else:
        return True
    
input = '()[]{}'
result = isValid(input)
print(result)