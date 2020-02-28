import re

NAME = r"[a-zA-Z_]\w*"


class sequence(object):
    def __init__(self, seq):
        self.seq = seq
        self.sp = 0
        self.mapping = {"kotlin": "java.lang", "Unit": "Void","Int":"Integer"}

    def getsp(self):
        return self.sp

    def setsp(self, sp):
        self.sp = sp

    def eat(self, r):
        m = re.match(r, self.seq[self.sp:])
        if m:
            self.sp += m.span()[1]
            return m.group()
        return ""

    def match(self, r):
        while self.eat(r" "):
            pass
        e = self.eat(r)
        if e in self.mapping:
            return self.mapping[e]
        return e

    def isEnd(self):
        while self.eat(r" "):
            pass
        return self.sp == len(self.seq)


def typeParam(seq):
    psp = seq.getsp()
    star = seq.match(r"\*")
    if star:
        return "?"
    covariance = seq.match(r"in |out ")
    if covariance:
        t = type1(seq)
        if t:
            cmap = {"in ": "? super ", "out ": "? extends "}
            return cmap[covariance] + t
    seq.setsp(psp)
    t = type1(seq)
    if t:
        return t
    return ""


def typeParams(seq):
    t = typeParam(seq)
    if not t:
        return ""
    psp = seq.getsp()
    if seq.match(r","):
        ts = typeParams(seq)
        if ts:
            return t+","+ts
    seq.setsp(psp)
    return t


def simpleUserType(seq):
    n = name(seq)
    if not n:
        return ""
    psp = seq.getsp()
    if seq.match(r"<"):
        t = typeParams(seq)
        if t:
            if seq.match(r">"):
                return n+"<"+t+">"
    seq.setsp(psp)
    return n


def userType(seq):
    s = simpleUserType(seq)
    if not s:
        return ""
    psp = seq.getsp()
    if seq.match(r"\."):
        u = userType(seq)
        if u:
            return s+"."+u
    seq.setsp(psp)
    return s


def name(seq):
    n = seq.match(NAME)
    return n


def parameters(seq):
    #    parameters     ::= type [ "," parameters ] -------->
    #    parameters     ::= type [ "," parameters ]
    t = type1(seq)
    if not t:
        return "",0
    psp = seq.getsp()
    if seq.match(r","):
        p,count = parameters(seq)
        if p:
            return t+","+p,count+1
    seq.setsp(psp)
    return t,1


def functionType(seq):
    # functionType   ::= "(" [ parameters ] ")" "->" type ------>
    # functionType   ::= "Function" ++ (number of parameters) "<" [ parameters "," ] type ">"
    psp = seq.getsp()
    if not seq.match(r"\("):
        return ""
    p,count = parameters(seq)
    if seq.match(r"\)"):
        if seq.match(r"->"):
            t = type1(seq)
            if t:
                return "Function"+str(count)+"<"+p+("," if p else "")+t+">"
    seq.setsp(psp)
    return ""


def type1(seq):
    psp = seq.getsp()
    f = functionType(seq)
    if f:
        return f
    seq.setsp(psp)
    u = userType(seq)
    if u:
        return u
    seq.setsp(psp)
    n = name(seq)
    if n:
        return n
    return ""


def transpile(input):
    seq = sequence(input)
    psp = seq.getsp()
    f = functionType(seq)
    if f and seq.isEnd():
        return f
    seq.setsp(psp)
    n = name(seq)
    if n and seq.isEnd():
        return n
    seq.setsp(psp)
    u = userType(seq)
    if u and seq.isEnd():
        return u
    return None

print(transpile("() ->"))
