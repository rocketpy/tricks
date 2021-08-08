#  Memoization
# This is an optimization method in which the result of the function execution is saved and this result is used in the next call. 

def memoize(f):
    cache = {}

    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate
  
  
  
