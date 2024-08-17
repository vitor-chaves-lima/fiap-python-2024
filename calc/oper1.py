def sum(*params):
    res = 0
    for i in params:
        res += i
    return res

def sub(*params):
    res = params[0]
    for i in params[1:]:
        res -= i
    return res