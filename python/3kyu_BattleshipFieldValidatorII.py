import random
from datetime import datetime


def validate_battlefield(bf):
    count = 0
    for i in bf:
        for j in i:
            if j == 1:
                count += 1
    if count == 20:
        return battleship(bf)
    else:
        return False


def copy(bf):
    l = []
    for i in bf:
        l.append([j for j in i])
    return l


def battleship(bf):
    for i in range(0, len(bf)):
        for j in range(0, len(bf[i]) - 3):
            if bf[i][j] == 1 and bf[i][j + 1] == 1 and bf[i][j + 2] == 1 and bf[i][j + 3] == 1:
                new_bf = copy(bf)
                for k in range(0, 4):
                    new_bf[i][j + k] = 0
                re = cruisers(new_bf)
                if re:
                    return re
    for i in range(0, len(bf) - 3):
        for j in range(0, len(bf[i])):
            if bf[i][j] == 1 and bf[i + 1][j] == 1 and bf[i + 2][j] == 1 and bf[i + 3][j] == 1:
                new_bf = copy(bf)
                for k in range(0, 4):
                    new_bf[i + k][j] = 0
                re = cruisers(new_bf)
                if re:
                    return re
    return False


def cruisers(bf):
    l = []
    for i in range(0, len(bf)):
        for j in range(0, len(bf[i]) - 2):
            if bf[i][j] == 1 and bf[i][j + 1] == 1 and bf[i][j + 2] == 1:
                l.append([i, j, 0])
    for i in range(0, len(bf) - 2):
        for j in range(0, len(bf[i])):
            if bf[i][j] == 1 and bf[i + 1][j] == 1 and bf[i + 2][j] == 1:
                l.append([i, j, 1])
    if len(l) < 2:
        return False
    else:
        for i in range(0, len(l)):
            for j in range(i + 1, len(l)):
                new_bf = copy(bf)
                for k in range(0, 3):
                    if l[i][2] == 0:
                        new_bf[l[i][0]][l[i][1] + k] = 0
                    if l[j][2] == 0:
                        new_bf[l[j][0]][l[j][1] + k] = 0
                    if l[i][2] == 1:
                        new_bf[l[i][0] + k][l[i][1]] = 0
                    if l[j][2] == 1:
                        new_bf[l[j][0] + k][l[j][1]] = 0
                re = destroyers(new_bf)
                if re:
                    return re

    return False


def destroyers(bf):
    count = 0
    new_bf = copy(bf)
    for i in range(0, len(bf)):
        for j in range(0, len(bf[i]) - 1):
            if new_bf[i][j] == 1 and new_bf[i][j + 1] == 1:
                
                if count != 3:
                    new_bf[i][j] = 0
                    new_bf[i][j + 1] = 0
                    count += 1
                else:
                    break
    for i in range(0, len(bf) - 1):
        for j in range(0, len(bf[i])):
            if new_bf[i][j] == 1 and new_bf[i + 1][j] == 1:
                
                if count != 3:
                    new_bf[i][j] = 0
                    new_bf[i + 1][j] = 0
                    count += 1
                else:
                    break
    if count < 3:
        return False
    else:
        re = submarines(new_bf)
        if re:
            return re

    return False


def submarines(bf):
    count = 0
    for i in bf:
        for j in i:
            if j == 1:
                count += 1
    if count == 4:
        return True
    else:
        return False