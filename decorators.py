# def:
# addding functionality to existing functionality.
# def mydecorator():
#      def fun1():
#         return fun1.upper()
#         print(fun1(input("enter value:")))

###########################################

# def uppercase_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result.upper()
#     return wrapper
#
# @uppercase_decorator
# def greet(name):
#     return f"Hello, {name}!"
#
# # Test the decorated function
# result = greet("John")
# print(result)


########################################simple decorator example

# def mydecorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result.upper()
#     return wrapper
#
# @mydecorator
# def fun1(input_value):
#     return input_value
#
# # Test the decorated function
# result = fun1(input("Enter a value: "))
# print("Uppercase:", result)

######################################

# a = "mahi"
# print(a.upper())
# o/p:MAHI
##################################

# def func(a):
#     return a.upper()
# print(func("monika"))
# o/p:MONIKA

#######################
# Define a decorator function
# def print_function_name(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling function: {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper
#
# # Apply the decorator to a function
# @print_function_name
# def greet(name):
#     return f"Hello, {name}!"
#
# # Call the decorated function
# print(greet("Alice"))

