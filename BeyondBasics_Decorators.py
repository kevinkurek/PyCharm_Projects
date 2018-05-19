# Decorators

def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs) # Has to be CALLABLE!!!
        return ascii(x)

    return wrap # Has to return a CALLABLE


# Without Decorator
def northern_city():
    return 'Tromsø'

print(northern_city())


# With Decorator
@escape_unicode
def northern_city():
    return 'Tromsø'

print(northern_city())




# Can use classes as decorators since they're callable
class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)

@CallCount
def hello(name):
    print('Hello, {}'.format(name))

hello('kevin')
hello('alex')
hello('ava')
print(hello.count)




# Class Instance as decorators
class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args,**kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args,*kwargs)
        return wrap

tracer = Trace()
#tracer.enabled = False # This toggles if tracing is on or off

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]

l = [1,2,3]
l = rotate_list(l)
print(l)



# Multiple Decorators
def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap

class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args,**kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args,*kwargs)
        return wrap

@tracer
@escape_unicode
def island_makers(name):
    return name + 'øy'

print(island_makers('Llama'))




# Decorators on Methods
class IslandMaker:
    def __init__(self, suffix):
        self.suffix = suffix

    @tracer
    def make_island(self,name):
        return name + self.suffix

im = IslandMaker(' Island')
print(im.make_island('Python'))




# Functools.wraps for inheriting correct names of callable objects going into decorator
import functools
def noop(f):
    @functools.wraps(f)
    def noop_wrapper():
        return f()
    return noop_wrapper

@noop
def hello():
    """Print a well-known message."""
    print('Hello, World!')
    return

print(help(hello))