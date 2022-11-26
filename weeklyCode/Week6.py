# Positional Arguments
def func(name, action, name1):
    print(name, action, name1)
func("Tien", "punch", "you") # Tien punch you


# Keyword Argument
def nextfunc(name, action):
    print(name, action)
nextfunc(name='Tien', action='code') # Tien code
nextfunc(action='code', name='Tien') # Tien code


# Default Argument
def thenfunc(name, action='sleep'):
    print(name, action)
thenfunc('Tien', 'play') # Tien play
thenfunc('Tien')         # Tien sleep


# Variable Length Positional Arguments
# Use this type of argument if you don't know exactly the number of 
# input arguments => turn it to tuple
def firstfunc(*args):
    print(args[1] + args[2])
firstfunc(1, 2, 3, 4, 5) # 5


# Variable Length Keyword Arguments
# Collect input variables and turn they into a dict
def  secfunc(**args):
    print(args)
secfunc(name='Tien', age='19', job='student') # {'name': 'Tien', 'age': '19', 'job': 'student'}


# Python is able to return multiple value by using , between the returned
# values => Returned value : a tuple
def thifunc(a, b):
    return a + b, a - b
x = thifunc(5, 2)
print(x) # (7, 3) (a tuple)


# Describe the function
def foufunc(a,b):
    """
    This function returns the sum of a and b
    """
    print(a + b)
# use help(function's name)
help(foufunc)
# use __doc__ attribute
print(func.__doc__)


# Nested function
def outer(a, b):
    def inner(c ,d):
        return c + d
    return inner(a, b)
result = outer(2, 4)
print(result) # 6


# Assign function with other name
def hello():
    print("hello")
hi = hello
hi()


# def is a command, so it appears anywhere in the code
x = 0
if x:
    def hello():
        print("hello tien")
else:
    def hello():
        print("hello")
hello()


# To change value of global variable in function, we need to use
# global or globals function
x = 42
def myfunc():
    global x
    x = 0
    print(x)
myfunc()
print(x)


# enclosing scope : use nonlocal to change the value
def f1():
    x =  42
    def f2():
        nonlocal x
        x = 0
        print(x)
    f2()
    print(x)
f1()