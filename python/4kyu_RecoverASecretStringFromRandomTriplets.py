def recoverSecret(triplets):
    s = set()
    for i in triplets:
        for j in i:
            s.add(j)

    def loop(st, n):
        for i in s:
            if st.find(i) != -1:
                continue
            newst = st + i
            flag = True
            for j in triplets:
                j0 = newst.find(j[0]) if newst.find(j[0]) != -1 else 10000
                j1 = newst.find(j[0]) if newst.find(j[1]) != -1 else 10000
                j2 = newst.find(j[0]) if newst.find(j[2]) != -1 else 10000
                if j0 > j1 or j1 > j2 or j0 > j2:
                    flag = False
                    break
            if flag:
                if n == len(s)-1:
                    return newst
                else:
                    ret = loop(newst, n + 1)
                    if ret == '':
                        continue
                    else:
                        return ret
        return ''

    return loop('',0)