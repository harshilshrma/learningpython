# Lambda Functions or Anonymous Functions
#

# minus = lambda x, y: x-y
#
# def minus(x, y):
#     return x-y
#
# print(minus(3,2))

def a_first(a):
    return a[1]

a = [[1, 14], [5, 6], [8, 23]]
a.sort(key=a_first)   #or remove the function and replace a_first with: "lambda x:x[1]"
print(a)
