def mean(x):
    s = 0
    for xi in x:
        s += xi
    return s / len(x)

def tong(x):
    s = 0
    for xi in x:
        s += xi**2

    return s
