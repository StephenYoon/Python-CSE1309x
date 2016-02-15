# GCD
def find_gcd(some_list):
    gcd_check = 1
    gcd = 1
    
    while (gcd_check <= max(some_list)):
        
        valid = True
        for value in some_list:
            if (value%gcd_check != 0):
                valid = False

        if(valid):
            gcd = gcd_check
        
        gcd_check = gcd_check + 1
        
    return gcd