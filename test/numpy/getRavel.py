def getRavel(alist, order):
    ret = []
    #  ‘F’ means to index the elements in column-major, Fortran-style order
    if order == 'F':
        cols = len(alist[0])
        n=0
        for i in range(cols):
            for m in range(len(alist)):
                ret.append(alist[m][i])
                n+=1
    return ret