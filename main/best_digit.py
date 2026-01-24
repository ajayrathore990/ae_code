
def best_digit(digit ,num_str):
    stack =[]
    for d in num_str:
        while digit > 0 and len(stack)>1 and  d> stack[len(stack)-1]: 
            digit= digit -1
            stack.pop()
        stack.append(d)
    while digit>0:
        digit = digit -1
        stack.pop()
        
    return "".join(stack)


    