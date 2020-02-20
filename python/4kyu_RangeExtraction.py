def solution(a):
    i = 0
    re = []
    while i < len(a):
        j = i
        while j < len(a) + 1:
            if j < len(a) and a[i] - a[j] == i - j:
                j += 1
                continue
            else:
                if j - i > 2:
                    re.append("{}-{}".format(a[i], a[j - 1]))
                elif j - i == 2:
                    re.append(str(a[i]))
                    re.append(str(a[i + 1]))
                else:
                    re.append(str(a[i]))
                break
        i = j
    return ",".join(re)