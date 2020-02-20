from functools import reduce


def part(n):
    s = set()

    def fun(l):
        if len(l) > 1:
            s.add(reduce(lambda x, y: x * y, l))
        else:
            s.add(l[0])
        if len(l) > 1 and l[-1] == l[-2]:
            return
        if len(l) == 1:
            left = 1
        else:
            left = l[-2]
        right = l[-1]
        for i in range(left, right // 2 + 1):
            nl = [j for j in l]
            nl[-1] = i
            nl.append(right - i)
            fun(nl)
        return

    fun([n])
    s = sorted(s)
    ran = s[-1] - 1
    if len(s) > 1:
        mean = float(reduce(lambda x, y: x + y, s)) / len(s)
    else:
        mean = s[0]
    if len(s) % 2:
        mid = s[len(s) / 2]
    else:
        mid = float((s[len(s) / 2] + s[len(s) / 2 - 1])) / 2
    return 'Range: %d Average: %.2f Median: %.2f' % (ran, mean, mid)