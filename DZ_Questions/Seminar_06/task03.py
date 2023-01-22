# def sum(x, y):
#     return x + y
#
#
# def div(x, y):
#     return x - y
#
#
# def mult(x, y):
#     return x * y
#
#
# def diff(x, y):
#     return x / y
#
#
# def calc(op, a, b):
#     print(op(a, b))
#
#
# calc(sum, 3, 2)
# calc(div, 3, 2)
# calc(mult, 3, 2)
# calc(diff, 3, 2)


def calc(op, a, b):
    print(op(a, b))


calc(lambda x, y: x+y, 6, 5)
calc(lambda x, y: x-y, 44, 19)
calc(lambda x, y: x*y, 4, 5)
calc(lambda x, y: x/y, 21, 7)



