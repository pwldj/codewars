def dig_pow(n, p):
    l = [int(i) for i in str(n)]
    count=0
    for i in l:
        count+=i**p
        p+=1
    
    return count//n if count%n==0 else -1