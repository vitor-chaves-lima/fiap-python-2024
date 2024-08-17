def mult(*params):
    res = 1
    for i in params:
        res *=i
    return res

def div(*params):
    res = params[0]
    for i in params[1:]:
        if i == 0:
            continue
        res /= i
    return res