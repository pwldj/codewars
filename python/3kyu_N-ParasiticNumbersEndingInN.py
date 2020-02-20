def calc_special(lastDigit, base):
    for i in range(2, 1000):
        if (base ** i - lastDigit) % (base * lastDigit - 1) == 0:
            for b in range(lastDigit, base):
                a = b * (base ** i - lastDigit) / (base * lastDigit - 1)
                if lastDigit * (base * a + b) == b * (base ** i) + a:
                    return format(base * a + b, base)


def format(n, base):
    m = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    re = ''
    while n:
        re = m[n % base] + re
        n = n / base
    return re