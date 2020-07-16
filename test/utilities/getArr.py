def getArr(row, cols):
    return [[0 for x in range(cols)] for x in range(row)]
try:
    import chardet
except ImportError:
    chardet = None