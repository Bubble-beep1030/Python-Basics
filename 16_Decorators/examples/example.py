def deco(fn):
    def wrap(*a, **k):
        return fn(*a, **k)
    return wrap
