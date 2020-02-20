def next_smaller(n):
    l = [int(i) for i in str(n)]
    l1 = []
    flag = True
    for i in range(len(l) - 2, -1, -1):
        if l[i] > l[i + 1]:
            max = i + 1
            for j in range(i + 1, len(l)):
                if l[i] > l[j] > l[max]:
                    max = j
            l[i],l[max]=l[max],l[i]
            l1 = l[:i+1] + sorted(l[i + 1:], reverse=True)
            flag = False
            break
    if flag or l1[0] == 0:
        return -1
    return int("".join([str(i) for i in l1]))