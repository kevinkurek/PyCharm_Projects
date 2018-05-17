# inner is called a 'local function' because it's defined
# within the outer function. They are no different from any other object
# (like a variable) inside a normal function.
g = 'global'
def outer(p='param'):
    l = 'local'
    def inner():
        print(g, p, l)
    inner()
outer()


# Closures are what keep the scopes of multiple functions alive.
# It essentially maintains references to objects from earlier scopes
# within the LEGB rule.
def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp

square = raise_to(2) # This creates a closure so the local function has access to the initial parameters
print(square(5))
cube = raise_to(3)
print(cube(5))


# Global scope within closure of nested functions.
message = 'global'

def enclosing():
    message = 'enclosing'

    def local():
        global message
        message = 'local'

    print('Enclosing message:', message)
    local()
    print('Enclosing message:', message)

print('global message:', message)
enclosing()
print('global message:', message)


# Using nonlocal to change enclosing message
message = 'global'

def enclosing():
    message = 'enclosing'

    def local():
        nonlocal message
        message = 'local'

    print('Enclosing message:', message)
    local()
    print('Enclosing message:', message)

print('global message:', message)
enclosing()
print('global message:', message)