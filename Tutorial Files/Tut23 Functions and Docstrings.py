# a = 9
# b = 8
# c = sum((a, b))              #Built-in function

# def function1():             #User defined function
#     print("Hello you're in function1.")
# function1()
# function1()
# function1()
# function1()

def function1(a, b):
    print("Hello you're in function1:", a+b)
#saada func, without input/output, returns nothing/no value

def function2(a, b): #function ke andar,pehle line mein pe jo string likhi hoti hai,use docstring bolte hein
    """This is a function which will calculate average of two numbers."""
    average = (a+b)/2
    # print(average)
    return average

v = function2(4, 8)
print(v)
#print(function2.__doc__)