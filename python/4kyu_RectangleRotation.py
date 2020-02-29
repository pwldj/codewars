def rectangle_rotation(a, b):
    l = a // (2 ** 0.5) * 2 + 1
    h = b // (2 ** 0.5) * 2 + 1
    if (l + h) % 4 == 0:
        return int((l//2+1) * (h // 2) + (l//2) * (h // 2 + 1))
    else:
        return int((l//2) * (h // 2) + (l//2 + 1) * (h // 2 + 1))