def solve(s, ops):
    his = [[(-1, -1) for i in range(len(ops)+1)] for j in range(len(ops)+1)]

    def fun(s, ops, l, r):
        if l == r:
            if s[l] == 't':
                return 1, 0
            else:
                return 0, 1
        at, af = 0, 0
        for m in range(l, r):
            if his[l][m] == (-1, -1):
                his[l][m] = fun(s, ops, l, m)
            if his[m + 1][r] == (-1, -1):
                his[m + 1][r] = fun(s, ops, m + 1, r)
            lt, lf = his[l][m]
            rt, rf = his[m + 1][r]
            if ops[m] == '&':
                at += lt * rt
                af += ((lt + lf) * (rt + rf) - lt * rt)
            if ops[m] == '|':
                at += ((lt + lf) * (rt + rf) - lf * rf)
                af += lf * rf
            if ops[m] == '^':
                at += (lt * rf + lf * rt)
                af += (lt * rt + lf * rf)
        return at, af

    return fun(s, ops, 0, len(ops))[0]