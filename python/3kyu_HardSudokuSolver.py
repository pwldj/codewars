import copy


def solve(puzzle):
    r = []

    def cast(puzzle):
        s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        map = {}
        for i in range(0, 9):
            for j in range(0, 9):
                if puzzle[i][j] == 0:
                    num = set(puzzle[i]) | (set(x[j] for x in puzzle))
                    sc = i // 3
                    sl = j // 3
                    for ii in range(0, 3):
                        for jj in range(0, 3):
                            if puzzle[sc * 3 + ii][sl * 3 + jj]!=0:
                                num.add(puzzle[sc * 3 + ii][sl * 3 + jj])
                    map[int(str(i) + str(j))] = s - num
        return map

    def fun(p):
        pu = []
        for i in p:
            pu.append([j for j in i])
        m = cast(pu)
        if len(m) == 0:
            #if len(r) == 1:
                #raise Exception('invalid grid')
            r.append(pu)
            return 're'
        min_v, min_k = min(zip((len(x) for x in m.values()), m.keys()))
        if min_v == 0:
            return
        for n in m[min_k]:
            pu[min_k // 10][min_k % 10] = n
            re = fun(pu)
            if re is not None and len(m) > 4:
                    return 're'

    for i in range(0, 9):
        for j in range(0, 9):
            if puzzle[i][j] != 0:
                m = set()
                for k in range(0, 9):
                    if puzzle[i][k] != 0 and puzzle[i][k] in m:
                        raise Exception('invalid grid')
                    m.add(puzzle[i][k])
                m = set()
                for k in range(0, 9):
                    if puzzle[k][j] != 0 and puzzle[k][j] in m:
                        raise Exception('invalid grid')
                    m.add(puzzle[k][j])
                m = set()
                sc = i // 3
                sl = j // 3
                for ii in range(0, 3):
                    for jj in range(0, 3):
                        if puzzle[sc * 3 + ii][sl * 3 + jj] != 0 and puzzle[sc * 3 + ii][sl * 3 + jj] in m:
                            raise Exception('invalid grid')
                        m.add(puzzle[sc * 3 + ii][sl * 3 + jj])

    if len(puzzle) != 9:
        raise Exception('invalid grid')
    for i in puzzle:
        if len(i) != 9:
            raise Exception('invalid grid')
        for j in i:
            if j > 9 or j < 0:
                raise Exception('invalid grid')
    fun(puzzle)

    return r[0]