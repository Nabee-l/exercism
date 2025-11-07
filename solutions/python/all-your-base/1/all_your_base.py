def rebase(input_base, digits, output_base):
    n1 = input_base
    n2 = output_base

    if n1 < 2:
        raise ValueError("input base must be >= 2")
    if n2 < 2:
        raise ValueError("output base must be >= 2")
        

    exp = len(digits) - 1  
    og =0
    for d in digits:
        if not 0 <= d < n1:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        og += d*(n1**exp)
        exp -= 1
        
    sum = []   
    while og > 0:
        digit = og % n2
        sum.append(digit)
        og = og//n2
    sum.reverse()
    if sum == []:
        sum = [0]
    return sum 
    
    
        
