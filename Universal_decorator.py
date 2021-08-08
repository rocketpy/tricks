# universal decorator for any number of arguments

def memoize(f):
    cache = {}

    def decorate(*args, **kwargs):
        key = (tuple(args), hash(tuple(sorted(kwargs.items()))))
        if key not in cache:
            cache[key] = f(*args, **kwargs)
        return cache[key]

    return decorate
