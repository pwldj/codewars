from functools import reduce


def listPosition(word):
    fac = lambda l, r: reduce(lambda x, y: x * y, range(l, r + 1))
    count = 0
    while word:
        deno = fac(1, len(word))
        nume = 1
        for j in set(word):
            nume *= fac(1, word.count(j))
        arr_len = deno // nume
        sort = sorted(word)
        count += arr_len * sort.index(word[0]) // len(word)
        word = word[1:]
    return count+1