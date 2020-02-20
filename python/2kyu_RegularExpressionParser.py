class AST(object):
    pass


class Normal(AST):
    def __init__(self, token):
        self.value = token

    def __str__(self):
        return self.value


class Any(AST):
    def __init__(self):
        pass

    def __str__(self):
        return "."


class ZeroOrMore(AST):
    def __init__(self, left):
        self.value = left

    def __str__(self):
        return str(self.value) + "*"


class Or(AST):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + str(self.left) + "|" + str(self.right) + ")"


class Str(AST):
    def __init__(self, l):
        self.l = l

    def __str__(self):
        return "(" + "".join([str(i) for i in self.l]) + ")"


def c(l, i):
    if l[i] not in ["(", ")", "|", "*"]:
        return Normal(l[i]), i + 1
    elif l[i] == "(":
        n, i = expr(l, i + 1)
        if l[i] == ")":
            return n, i + 1
        else:
            raise Exception()


def t(l, i):
    n, i = c(l, i)
    if i < len(l) and l[i] == '*':
        n = ZeroOrMore(n)
        i += 1
        if i < len(l) and l[i] == '*':
            raise Exception()
    return n, i


def f(l, i):
    p = []
    while i < len(l) and l[i] != '|' and l[i] != ")":
        n, i = t(l, i)
        p.append(n)
    if len(p) == 0:
        raise Exception()
    elif len(p) == 1:
        return p[0], i
    else:
        return Str(p), i


def expr(l, i):
    n, i = f(l, i)
    if i < len(l) and l[i] == '|':
        n2, i = f(l, i + 1)
        n = Or(n, n2)
        if i < len(l) and l[i] == '|':
            raise Exception()

    return n, i


def parseRegExp(input):
    if input == '':
        return ''
    i = 0
    n = AST()
    try:
        n, i = expr(input, i)
    except:
        print()

    if i != len(input):
        return ""
    else:
        return str(n)