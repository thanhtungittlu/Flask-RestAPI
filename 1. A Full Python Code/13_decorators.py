import functools  # function tools

def my_decorator(f):
    @functools.wraps(f)
    def function_that_runs_f():
        print("Hello!")
        f()
        print("After!")
    return function_that_runs_f

@my_decorator
def my_function():
    print("I'm in the function.")

my_function()