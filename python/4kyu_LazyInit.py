import types
def deco(f):
    def wrapper(*args, **kwargs):
        m = dict(zip(f.__code__.co_varnames,args))
        self = m['self']
        del m['self']
        self.__dict__.update(m)

    return wrapper


class LazyInit(type):
    def __new__(cls, *args, **kwargs):
        init = args[2]['__init__']
        f = deco(init)
        args[2]['__init__'] = f
        return type.__new__(cls, *args, **kwargs)

    pass