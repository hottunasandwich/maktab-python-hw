def multi_v1(*args):
    if args[-1] not in ['*', '+', '-', '/', '%', '**', '//', '<<', '>>', '^', '&', '|']:
        raise TypeError(f'{args[-1]} is not a valid operator')
    
    symbol = args[-1]

    for i in range(len(args) - 1):
        if type(args[i]) not in [float, int]:
            raise TypeError(f'{args[i]} is not an int or float')

    q = [str(i) for i in args[:-1]]
    return eval(f"{symbol.join(q)}")

# def dec(*args):
#     res = args[0]

#     for i in range(len(args) - 1):
#         res -= args[i + 1]

#     return res

# def multi(*args):
#     res = args[0]

#     for i in range(len(args) - 1):
#         res *= args[i + 1]

#     return res

# def div(*args):
#     res = args[0]

#     for i in range(len(args) - 1):
#         res /= args[i + 1]

#     return res

# def mod(*args):
#     res = args[0]

#     for i in range(len(args) - 1):
#         res %= args[i + 1]

#     return res

# def p(*args):
#     res = args[0]

#     for i in range(len(args) - 1):
#         res **= args[i + 1]

#     return res


# def multi_v2(*args):
#     op = args[-1]

#     return operators[op](*args[:-1])    


# def mysum(*args):
#     res = args[0]

#     for i in range(len(args) - 1):
#         res += args[i + 1]

#     return res

# operators = {
#     '+': mysum,
#     '-': dec,
#     '*': multi,
#     '/': div,
#     '%': mod,
#     '**': p
# }

print(multi_v1('s',2,3,4,'<<'))