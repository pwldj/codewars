def elder_age(m,n,l,t):
    if m>n:
        return elder_age(n,m,l,t)
    ml = []
    nl = []
    temp = 1
    while m>=temp or n>=temp:
        if temp&m:
            ml.append(temp)
        if temp&n:
            nl.append(temp)
        temp*=2
    
    ml.reverse()
    nl.reverse()

    re = 0
    lt = [0,0]
    for i in ml:
        for j in nl:
            if i==1 and j==1:
                mid = lt[0]^lt[1]
                if mid>l:
                    re+=mid-l
                lt = [lt[0],lt[1]+j]
                break
            if i>j:
                mid = ((lt[0]^lt[1])+((lt[0]+i-1)^lt[1]))//2
            else:
                mid = ((lt[0]^lt[1])+(lt[0]^(lt[1]+j-1)))//2

            b = max(i,j)
            s = min(i,j)
            r = [mid - (b-1)//2,mid + (b-1)//2+1]
            if r[1]<l:
                lt = [lt[0],lt[1]+j]
                continue
            c = r[1]-l+1 if r[0]<l else b
            r = [r[0]-l if r[0]>l else 0,r[1]-l if r[1]>l else 0]
            c=s*c
            fuck = ((int(r[0])+int(r[1]))*int(c))>>1
            re=re+fuck%t
            # re += int((int(r[0])+int(r[1]))*c)%t
            lt = [lt[0],lt[1]+j]
        lt = [lt[0]+i,0]


    return re%t