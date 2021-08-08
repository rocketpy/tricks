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
  
  
# Currying
# Currying is the transformation of a function from many arguments into a set of functions, each of which is a function from one argument.
# We can pass some of the arguments to a function and get back a function that expects the rest of the arguments. 

def greet_curried(greeting):
    def greet(name):
        print(greeting + ', ' + name)
    return greet

greet_hello = greet_curried('Hello')

greet_hello('Jack')
greet_hello('John')

#just call greet_curried
greet_curried('Hi')('Bob') 
 
