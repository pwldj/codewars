import itertools

ret = None
def solve_puzzle(clues):
    global ret
    ret = []
    n = 7
    m = creat(n)
    possible = {}
    for i in range(n):
        clue_left, clue_right = clues[4 * n - 1 - i], clues[n + i]
        var_left = m[clue_left]
        var_right = set(map(lambda row: tuple(reversed(row)), m[clue_right]))
        possible[4 * n - i - 1] = var_left.intersection(var_right)
        possible[4 * n - i - 1] = set(
            [x for x in possible[4 * n - i - 1] if
             all([x[j] <= n + i + 1 - clues[j] and x[j] <= 2 * n - i - clues[3 * n - 1 - j] for j in range(n)])])

        clue_top, clue_btm = clues[i], clues[3 * n - 1 - i]
        var_top = m[clue_top]
        var_btm = set(map(lambda row: tuple(reversed(row)), m[clue_btm]))
        possible[i] = var_top.intersection(var_btm)
        possible[i] = set(
            [x for x in possible[i] if
             all([x[j] <= n + i + 1 - clues[4 * n - j - 1] and x[j] <= 2 * n - i - clues[n + j] for j in range(n)])])

    possible = sorted(possible.items(), key=lambda d: len(d[1]))
    ss = [[0] * n for x in range(n)]
    return [list(x) for x in cal(ss, possible, clues, n, 0)]


def copy(ss):
    return [[y for y in x] for x in ss]


def cal(ss, possible, clues, n, p):
    pos = possible[p][0]
    ava = possible[p][1]

    if pos < n:
        ll = [x[pos % n] for x in ss]
        for i in range(n):
            if len(ava) == 0:
                break
            if ll[i] == 0:
                s = set(ss[i]) | set(ll)
                ava = [x for x in ava if x[i] not in s]
            else:
                ava = [x for x in ava if x[i] == ll[i]]
    else:
        ll = ss[n - 1 - pos % n]
        for i in range(n):
            if len(ava) == 0:
                break
            if ll[i] == 0:
                s = set([x[i] for x in ss]) | set(ll)
                ava = [x for x in ava if x[i] not in s]
            else:
                ava = [x for x in ava if x[i] == ll[i]]
    for l in ava:
        new_ss = copy(ss)
        if pos < n:
            for x in range(n):
                new_ss[x][pos % n] = l[x]
        else:
            new_ss[n - 1 - pos % n] = l
        if all([y for x in new_ss for y in x]):
            if chack(new_ss, possible, n):
                return new_ss
            else:
                return
        re = cal(new_ss, possible, clues, n, p + 1)
        if re is not None:
            return re


def chack(ss, clues, n):
    m = {}
    for x in clues:
        m[x[0]] = x[1]
    for i in range(n):
        flag = False
        for x in m[4 * n - i - 1]:
            if x == tuple(ss[i]):
                flag = True
        if not flag:
            return False
        flag = False
        for x in m[i]:
            if x == tuple([x[i] for x in ss]):
                flag = True
        if not flag:
            return False
    return True


def creat(n):
    m = {}
    for i in range(n + 1):
        m[i] = set()
    for l in itertools.permutations(list(range(1, n + 1))):
        m[0].add(l)
        count, mix = 0, 0
        for i in l:
            if i > mix:
                count += 1
                mix = i
        m[count].add(l)
    return m