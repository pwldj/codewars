def yield_nums(num1, num2, seq1, seq2):
    yield num1+num2, '('+seq1+'+'+seq2+')'
    yield num1-num2, '('+seq1+'-'+seq2+')'
    yield num2-num1, '('+seq2+'-'+seq1+')'
    yield num1*num2, '('+seq1+'*'+seq2+')'
    if num2!=0:# and num1 % num2 == 0:
        yield num1/num2, '('+seq1+'/'+seq2+')'
    if num1!=0:# and num2 % num1 == 0:
        yield num2/num1, '('+seq2+'/'+seq1+')'


def l3(nums, seqs):
    for num, seq in yield_nums(nums[0], nums[1], seqs[0], seqs[1]):
        if num == 24:
            return seq
    return None


def l2(nums, seqs):
    for i1, i2, i3 in [(0, 1, 2), (0, 2, 1), (1, 2, 0)]:
        for num, seq in yield_nums(nums[i1], nums[i2], seqs[i1], seqs[i2]):
            re = l3([num, nums[i3]], [seq, seqs[i3]])
            if re != None:
                return re
    return None


def l1(nums, seqs):
    for i1, i2, i3, i4 in [(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2), (1, 2, 0, 3), (1, 3, 0, 2), (2, 3, 0, 1)]:
        for num, seq in yield_nums(nums[i1], nums[i2], seqs[i1], seqs[i2]):
            re = l2([num, nums[i3], nums[i4]], [seq, seqs[i3], seqs[i4]])
            if re != None:
                return re
    return "It's not possible!"


def equal_to_24(a, b, c, d):
    return l1([a, b, c, d], [str(a), str(b), str(c), str(d)])


print(equal_to_24(4,3,1,6))
