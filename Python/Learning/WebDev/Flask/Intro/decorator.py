import time



def add(n1,n2):
    return n1+n2

def multiply(n1,n2):
    return n1*n2

def subtract(n1,n2):
    return n1-n2

def divide(n1,n2):
    return n1/n2

def calculate(calc_func,n1,n2):
    return calc_func(n1,n2)


result = calculate(add,32,12)
print(result)

def outer_function():
    print("I'm Outer")
    def inner():
        print("I'm Inner")

    inner()
# outer_function()

# Return a function from another function

def outer_func():
    print("I'm Outer")
    def inner_func():
        print("I'm Inner")
    return inner_func()






#Decorators
def delay_decorator(function):
    def wrapper():
        time.sleep(5)
        print("Delay Decorator used")
        function()
    return wrapper

#eg.
@delay_decorator
def say_hello():
    print("hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_():
    print("NO DECORATOR")
say_bye()
say_hello()
say_()