import math
def linspace(start, end, num, endpoint=True,retstep=False):
    divisor=num-1 if endpoint else num
    variation = (end - start) / divisor
    l = []
    for i in range(num):
        l.append(i * variation + start)
    return (l,divisor) if retstep else l
    