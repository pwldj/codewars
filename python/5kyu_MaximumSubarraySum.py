def maxSequence(arr):
    if len(arr) == 0:
        return 0
    sum = arr[0]
    l = 0
    r = l + 1

    while l < len(arr):
        temp = 0
        for i in range(r, len(arr)):
            temp += arr[i]
            if temp > 0:
                r = i + 1
                temp = 0
        temp = 0
        for i in range(l, r):
            temp += arr[i]
            if temp < 0:
                l = i+1
                temp = 0

        temp = 0
        for i in range(l, r):
            temp += arr[i]

        if sum < temp:
            sum = temp

        l = l + 1
        r = l + 1

    return sum