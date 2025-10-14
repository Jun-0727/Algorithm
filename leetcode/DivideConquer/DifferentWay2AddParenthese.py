def differentWay2AddParentheses(exp: str) -> list:
    
    def compute(left, right, op):
        result.append(eval(str(left) + op + str(right)))
        return result
        

    if exp.isdigit():
        return [int(exp)]

    result = [] 
    for i, value in enumerate(exp):
        if value in "+-*/":
            
            left = differentWay2AddParentheses(exp[:i])
            right = differentWay2AddParentheses(exp[i+1:])

            result.extend(compute(left, right, value)) 
    
    return result
print(differentWay2AddParentheses("2*3-4*5"))