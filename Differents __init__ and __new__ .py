# Docs: https://docs.python.org/3/reference/datamodel.html#object.__new__
# Article: https://howto.lintel.in/python-__new__-magic-method-explained/

"""
__new__() is intended mainly to allow subclasses of immutable types (like int, str, or tuple) to customize instance creation.
It is also commonly overridden in custom metaclasses in order to customize class creation.
"""
# Usual class declaration and instantiation

class Foo(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def bar(self):
        pass
    
# i = Foo(2, 3)


# A class implementation with __new__ method overridden

class Foo(object):
    def __new__(cls, *args, **kwargs):
        print "Creating Instance"
        instance = super(Foo, cls).__new__(cls, *args, **kwargs)
        return instance

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def bar(self):
        pass

# OutPut:
# i = Foo(2, 3)
# Creating Instance


# Things to remember
"""
If __new__ return instance of  it’s own class, then the __init__ method of newly created instance will be invoked
with instance as first (like __init__(self, [, ….]) argument following by arguments
passed to __new__ or call of class.  So, __init__ will called implicitly.

If __new__ method return something else other than instance of class,  then instances __init__ method will not be invoked.
In this case you have to call __init__ method yourself.
"""


