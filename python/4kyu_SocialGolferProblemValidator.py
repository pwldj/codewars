def valid(a):
    match = {}
    al = len(a[0])
    for i in a:
        lmem = []
        if len(i)!= al:
            return False
        jl = len(i[0])
        for j in i:
            if len(j)!=jl:
                return False
            for k in j:
                if ord(k) - len(''.join(i)) >= ord('A'):
                    return False
                if k in lmem:
                    return False
                else:
                    lmem.append(k)
                if k in match.keys():
                    for l in match[k]:
                        if l in j:
                            return False
                else:
                    match[k]=[]
                for l in j:
                    if l != k:
                        match[k].append(l)

    return True