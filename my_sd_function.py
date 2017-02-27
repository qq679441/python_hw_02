import math 
def dev(input_list):
    N=len(input_list)
    summation=0
    
    for i in input_list:
        summation+=i
        mean=summation/N
        
    variance=0
    for i in input_list:
        variance+=(i-mean)**2
    return math.sqrt(variance/N)
dev(range(2))
