def cut(cake):
    cake = cake.split('\n')
    cake_line = [j for i in cake for j in i]

    n = cake_line.count('o')
    if len(cake_line) % n != 0:
        return []
    cake_size = len(cake_line) // n
    row = len(cake)
    col = len(cake[0])

    def find(cake, row, col):
        for i in range(row):
            for j in range(col):
                if cake[i][j] == 'o' or cake[i][j] == '.':
                    return i, j

    def fun(cake, cake_size, row, col, full):
        r_start, c_start = find(cake, row, col)

        for c_size in range(col - c_start + 1, 0, -1):
            if cake_size % c_size == 0:
                r_size = cake_size // c_size
                if r_start >= 0 and c_start >= 0 and r_start + r_size <= row and c_start + c_size <= col:
                    if [cake[i][j] for i in range(r_start, r_start + r_size) for j in range(c_start, c_start + c_size)].count('.') == cake_size - 1:
                        cake_copy = [[j for j in i] for i in cake]
                        for i in range(r_start, r_start + r_size):
                            for j in range(c_start, c_start + c_size):
                                cake_copy[i][j] = full
                        if [j for i in cake_copy for j in i].count('.') == 0:
                            return cake_copy
                        else:
                            re = fun(cake_copy, cake_size, row, col, full + 1)
                            if re is not None:
                                return re
        return

    c_copy = fun(cake, cake_size, row, col, 0)
    if c_copy is None:
        return []
    re = []
    for num in range(n):
        c_slide = []
        for i in range(row):
            cake_ss = []
            for j in range(col):
                if c_copy[i][j] == num:
                    cake_ss.append(cake[i][j])
            if len(cake_ss) != 0:
                c_slide.append("".join(cake_ss))
        re.append('\n'.join(c_slide))

    return re