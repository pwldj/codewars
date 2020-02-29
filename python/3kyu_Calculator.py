class Calculator(object):
    @staticmethod
    def evaluate(s):
        if s == '':
            return 0
        num = []
        sym = []
        s = s.split(' ')
        i = 0
        while i < len(s):
            if s[i] == '+' or s[i] == '-':
                sym.append(s[i])
            elif s[i] == '*':
                num.append(num.pop() * float(s[i + 1]))
                i += 1
            elif s[i] == '/':
                num.append(num.pop() / float(s[i + 1]))
                i += 1
            else:                
                num.append(float(s[i]))   
            i += 1

        sym.reverse()
        num.reverse()
        while len(num) != 1:
            c = sym.pop()
            if c == '+':
                num.append(num.pop() + num.pop())
            else:
                num.append(num.pop() - num.pop())

        return num[0]