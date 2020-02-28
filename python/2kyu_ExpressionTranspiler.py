class Tokens(object):
    def __init__(self, seq):
        self.seq = seq
        self.sp = 0

    def removespace(self):
        while(self.sp < len(self.seq) and (self.seq[self.sp] == " " or self.seq[self.sp] == "\n")):
            self.sp += 1
        

    def eat(self, token):
        self.removespace()
        if self.sp < len(self.seq):
            t = self.seq[self.sp]
        else:
            return ""
        if t == token:
            self.sp += 1
            return t
        return ""

    def getnn(self):
        self.removespace()
        if self.sp >= len(self.seq) - 1:
            return ""
        fp = self.sp
        while(fp < len(self.seq) and (self.seq[fp].isalpha() or self.seq[fp].isdigit() or self.seq[fp]=="_")):
            fp += 1
        re = self.seq[self.sp:fp]
        if re and (not re[0].isdigit() or re.isdigit()):
            self.sp = fp
            return re
        return ""

    def isend(self):
        self.removespace()
        if self.sp == len(self.seq):
            return True
        return False


def lambdastmt(source):
    sp = source.sp
    nn = source.getnn()
    if not nn:
        source.sp = sp
        return ""
    stmt = lambdastmt(source)
    return nn+";"+stmt


def lambdaparam(source):
    sp = source.sp
    nn = source.getnn()
    if not nn:
        source.sp = sp
        return ""
    if source.eat(","):
        param = lambdaparam(source)
        if param:
            return nn+","+param
        else:
            source.sp = sp
            return ""
    return nn


def parameters(source):
    sp = source.sp
    expr = expression(source)
    if not expr:
        source.sp = sp
        return ""
    if source.eat(","):
        para = parameters(source)
        if para:
            return expr+","+para
        else:
            source.sp = sp
            return ""
    return expr


def lambda1(source):
    sp0 = source.sp
    if not source.eat("{"):
        source.sp = sp0
        return ""
    sp = source.sp
    param = lambdaparam(source)
    if param:
        if source.eat("-"):
            if not source.eat(">"):
                return ""
        else:
            source.sp = sp
            param = ""
    stmt = lambdastmt(source)
    if not source.eat("}"):
        source.sp = sp0
        return ""
    return "(" + param + "){" + stmt + "}"


def expression(source):
    sp = source.sp
    re = source.getnn()
    if re:
        return re
    re = lambda1(source)
    if re:
        return re
    source.sp = sp
    return ""


def function(source):
    target = ""
    expr = expression(source)
    if not expr:
        return ""
    para = ""
    if source.eat("("):
        para = parameters(source)
        if not source.eat(")"):
            return ""
        lam = lambda1(source)
    else:
        lam = lambda1(source)
        if not lam:
            return ""
    if lam and para:
        return expr + "(" + para + "," + lam + ")"
    else:
        return expr + "(" + para + lam + ")"


def transpile(expression):
    source = Tokens(expression)
    re = function(source)
    if re and source.isend():
        return re
    return ""


print(transpile("f(a,)"))
