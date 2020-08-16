def linear_search(values, search_for):
    search_at = 0
    search_res = False
# Match the value with each data element	
    while search_at < len(values) and search_res is False:
        if values[search_at] == search_for:
            search_res = True
        else:
            search_at = search_at + 1
    return search_res
def intpolsearch(values,x ):
    idx0 = 0
    idxn = (len(values) - 1)
    while idx0 <= idxn and x >= values[idx0] and x <= values[idxn]:
# Find the mid point
        mid = idx0 +\
               int(((float(idxn - idx0)/( values[idxn] - values[idx0]))
                    * ( x - values[idx0])))
                    # Compare the value at mid point with search value 
        if values[mid] == x:
            return (mid)
        if values[mid] < x:
            idx0 = mid + 1
    return False
def intpolsearch1(values, x):
    length=len(values)
    middle = length // 2
    while middle > 0 and middle < length:
        oldMiddle=middle
        midVal = values[middle]
        if midVal == x:
            return middle
        elif midVal > x:
            middle = middle // 2
        else:
            middle += (length - middle) // 2
        if oldMiddle == middle:
            break
    return False