class Extendtuple(tuple):

    def having(self, num):
        return Predicate(self, num)

    def __getattr__(self, item):
        if item == 'each':
            return self
        elif item in ['being_the', 'and_the']:
            return Predicate(self, item)


class Predicate(object):
    def __init__(self, obj, name):
        self.obj = obj
        self.name = name

    def __getattr__(self, item):
        if isinstance(self.obj, Extendtuple):
            if isinstance(self.name, int):
                re = []
                for th in self.obj:
                    if self.name == 1:
                        temp = Thing(item)
                        re.append(temp)
                    else:
                        temp = [Thing(item[0:-1])] * self.name
                        re = re + temp
                    setattr(th, item, temp)
                return Extendtuple(re)
            elif self.name in ['being_the', 'and_the']:
                return Predicate(self.obj, item)
            else:
                for thing in self.obj:
                    setattr(thing, self.name, item)
                return self.obj
        elif isinstance(self.name, int):
            if self.name == 1:
                temp = Thing(item)
            else:
                temp = Extendtuple([Thing(item[0:-1])] * self.name)
            setattr(self.obj, item, temp)
            return temp

        elif self.name == 'is_a':
            setattr(self.obj, "is_a_" + item, True)
            setattr(self.obj, "is_not_a_" + item, False)

        elif self.name == 'is_not_a':
            setattr(self.obj, "is_a_" + item, False)
            setattr(self.obj, "is_not_a_" + item, True)

        elif self.name == 'is_the':
            return Predicate(self.obj, item)

        elif self.name == 'can':
            def func(f, past=''):
                setattr(self.obj, past, [])
                def do(args):
                    getattr(self.obj, past).append(f(args))
                    return f(args)

                setattr(self.obj, item, do)

            return func

        else:
            setattr(self.obj, self.name, item)


class Thing(object):
    def __init__(self, name):
        self.name = name
        setattr(self, "is_" + name, True)

    def __getattr__(self, item):
        return Predicate(self, item)

    def has(self, num):
        return Predicate(self, num)

    def having(self, num):
        return Predicate(self, num)

    def __repr__(self):
        return self.name

    pass
name = "Jane"