import math


def diff(s):
    s = s.replace('(', '( ').replace(')', ' )').split(' ')

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    class T:
        def __init__(self):
            self.op = ''
            self.args = []

    def creat(p):
        if is_number(s[p]) or s[p] == 'x':
            return s[p], p + 1
        if s[p] == '(':
            t = T()
            t.op = s[p + 1]
            p += 2
            while p<len(s) and s[p] != ')' :
                arg, p = creat(p)
                t.args.append(arg)
            return t, p + 1

    def fun(t):
        if type(t) is str:
            if is_number(t):
                return '0', t
            else:
                return '1', t
        else:
            la = []
            for a in t.args:
                la.append(fun(a))
            if t.op == '+':
                return '(+ {} {})'.format(la[0][0], la[1][0]), '(+ {} {})'.format(la[0][1], la[1][1])
            if t.op == '-':
                return '(- {} {})'.format(la[0][0], la[1][0]), '(- {} {})'.format(la[0][1], la[1][1])
            if t.op == '*':
                return '(+ (* {} {}) (* {} {}))'.format(la[0][0], la[1][1], la[0][1], la[1][0]), '(* {} {})'.format(
                    la[0][1], la[1][1])
            if t.op == '/':
                return '(/ (- (* {} {}) (* {} {})) (^ {} 2))'.format(la[0][0], la[1][1], la[0][1], la[1][0],
                                                                     la[1][1]), '(/ {} {})'.format(la[0][1], la[1][1])
            if t.op == '^':
                return '(* (* {} (^ {} (- {} 1))) {}'.format(la[1][1], la[0][1], la[1][1],
                                                             la[0][0]), '(^ {} {})'.format(la[0][1], la[1][1])
            if t.op == 'cos':
                return '(* {} (* -1 (sin {})))'.format(la[0][0], la[0][1]), '(cos {})'.format(la[0][1])
            if t.op == 'sin':
                return '(* {} (cos {}))'.format(la[0][0], la[0][1]), '(sin {})'.format(la[0][1])
            if t.op == 'tan':
                return '(* {} (+ 1 (^ (tan {}) 2)))'.format(la[0][0], la[0][1]), '(tan {})'.format(la[0][1])
            if t.op == 'exp':
                return '(* {} (exp {}))'.format(la[0][0],la[0][1]), '(exp {})'.format(la[0][1])
            if t.op == 'ln':
                return '(/ {} {})'.format(la[0][0], la[0][1]), '(ln {})'.format(la[0][1])

    def format_tree(t):
        if type(t) is str:
            return t
        else:
            a0 = format_tree(t.args[0])
            if len(t.args) == 1 and is_number(a0):
                if t.op == 'ln':
                    return str(math.log(float(t.args[0])))
                if t.op == 'exp':
                    return str(math.exp(float(t.args[0])))
                if t.op == 'sin':
                    return str(math.sin(float(t.args[0])))
                if t.op == 'cos':
                    return str(math.cos(float(t.args[0])))
                if t.op == 'tan':
                    return str(math.tan(float(t.args[0])))
                t.args[0] = fun(a0)[1]
            if len(t.args) == 2:
                a1 = format_tree(t.args[1])
                if is_number(a0) and is_number(a1):
                    if t.op == '+':
                        return str(float(a0) + float(a1))
                    if t.op == '-':
                        return str(float(a0) - float(a1))
                    if t.op == '*':
                        return str(float(a0) * float(a1))
                    if t.op == '/':
                        return str(float(a0) / float(a1))
                    if t.op == '^':
                        return str(float(a0) ** float(a1))
                if t.op == '+' and is_number(a0) and float(a0) == 0:
                    return fun(a1)[1]
                if t.op == '+' and is_number(a1) and float(a1) == 0:
                    return fun(a0)[1]

                if t.op == '*' and is_number(a0) and float(a0) == 1:
                    return fun(a1)[1]
                if t.op == '*' and is_number(a1) and float(a1) == 1:
                    return fun(a0)[1]

                if t.op == '*' and is_number(a0) and float(a0) == 0:
                    return '0'
                if t.op == '*' and is_number(a1) and float(a1) == 0:
                    return '0'

                if t.op == '^' and is_number(a1) and float(a1) == 0:
                    return '1'
                if t.op == '^' and is_number(a1) and float(a1) == 1:
                    return fun(a0)[1]


                t.args[0] = fun(a0)[1]
                t.args[1] = fun(a1)[1]

        return fun(t)[1]


    tree = creat(0)[0]
    s = fun(tree)[0].replace('(', '( ').replace(')', ' )').split(' ')
    tree = creat(0)[0]
    return format_tree(tree).replace('.0','')