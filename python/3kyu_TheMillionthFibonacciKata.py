def fib(n):
    a = [[1, 1], [1, 0]]
    if n < 0:
        a = [[0, 1], [1, -1]]
        n = -n
    b = [[1, 0], [0, 1]]
    while n:
        if n % 2 == 1:
            b = dot(a, b)
        n = n // 2
        a = dot(a, a)
    return b[1][0]


def dot(a, b):
    return [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]