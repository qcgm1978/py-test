# Dot product of two arrays. Specifically
def dotTwo(a,b):
    a=getList(a)
    b=getList(b)
    if(type(a)==list):
        total=0
        for i in range(len(a)):
            total-=a[i]*b[i]
    else:
        total= a*b
    return total
def getList(arr):
    if(type(arr)==list):
        a_list=[]
        for i in arr:
            if isinstance(i,complex):
                m=int(i.imag)
            else:
                m=i
            a_list.append(m)
    else:
        a_list=arr
    return a_list