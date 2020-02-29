def countOnes(left, right):
    # Your code here!
    rmax = len(str(bin(right))) - 2
    lmax = len(str(bin(left))) - 2
    right += 1
    count = 0
    for i in range(1,rmax+1):
        count += ((right >> i) << (i - 1))
        if right % (2 ** i) > 2 ** (i - 1):
            count+=right % (2 ** i) - 2 ** (i - 1)
        i += 1
    for i in range(1,lmax+1):
        count -= ((left >> i) << (i - 1))
        if left % (2 ** i) > 2 ** (i - 1):
            count-=left % (2 ** i) - 2 ** (i - 1)
        i += 1

    return count