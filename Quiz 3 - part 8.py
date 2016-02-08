# return the number of chickens and number of dogs in the farm in a list 
def chickens_dogs(heads, legs):
    is_found = False
    for h in range(1,heads+1):
        total_legs = (h*2) + (heads-h)*4
        if (total_legs == legs):
            answer = [h, heads-h]
            is_found = True
            break

    if(is_found):
        return answer
    else:
        return None
    
