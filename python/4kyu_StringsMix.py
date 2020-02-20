import functools


def comp(v1, v2):
    m = {'1':3,'2':2,'=':1}
    if v1[1] != v2[1]:
        return v1[1] - v2[1]
    if v1[0][0] != v2[0][0]:
        return m[v1[0][0]] - m[v2[0][0]]
    return ord(v2[0][-1]) - ord(v1[0][-1])


def mix(s1, s2):
    m = {}
    for i in range(97, 123):
        c = chr(i)
        c1 = s1.count(c)
        c2 = s2.count(c)
        if c1 > 1 or c2 > 1:
            if c1 > c2:
                m['1:' + c * c1] = c1
            elif c1 < c2:
                m['2:' + c * c2] = c2
            else:
                m['=:' + c * c1] = c1
    m = sorted(m.items(), key=functools.cmp_to_key(comp), reverse=True)
    return "/".join([x[0] for x in m])