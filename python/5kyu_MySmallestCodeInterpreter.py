def brain_luck(code, input):
    point = 0
    ip = 0
    data = [0]*100
    output = ''
    ci = 0
    match = {}
    templist = []
    for temp in range(len(code)):
        if code[temp] == '[':
            templist.append(temp)
        if code[temp] == ']':
            match[temp] = templist[-1]
            match[templist[-1]] = temp
            templist.pop()

    while ci < len(code):
        if code[ci] == '>':
            point = (1 + point) % 256
        if code[ci] == '<':
            point = (point + 255) % 256
        if code[ci] == '+':
            data[point] = (data[point] + 1) % 256
        if code[ci] == '-':
            data[point] = (data[point] + 255) % 256
        if code[ci] == '.':
            output += chr(data[point])
        if code[ci] == ',':
            data[point] = (ord(input[ip]))
            ip += 1
        if code[ci] == '[' and data[point] == 0:
            ci = match[ci]
        if code[ci] == ']' and data[point] != 0:
            ci = match[ci]
        ci += 1


    return output