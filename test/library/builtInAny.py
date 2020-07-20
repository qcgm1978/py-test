def getAny(iterable):
    for element in iterable:
        if element:
            return True
    return False