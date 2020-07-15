# Dot product of two arrays. Specifically
def isComplexNum(i):
    num=i[0] if isinstance(i,list) else i
    return isinstance(num,complex)
def dotTwo(a,b):
    isComplex=isComplexNum(a)
    a=getList(a)
    b=getList(b)
    if(type(a)==list):
        total=0
        if(isComplex):
            for i in range(len(a)):
                total-=a[i]*b[i]
        else:
            row = len(a)
            cols = len(b[0])
            total = [[0 for x in range(cols)] for x in range(row)] 
            for i in range(len(a)):
                lenM=len(a[i])
                for m in range(lenM):
                    tot=ind=0
                    for n in range(cols):
                        tot+=a[i][n]*b[m][n]
                    total[m][i]=(tot)
    else:
        total= a*b
    return total

def getList(arr):
    if(type(arr)==list):
        a_list=[]
        for i in arr:
            if isComplexNum(i):
                m=int(i.imag)
            else:
                m=i
            a_list.append(m)
    else:
        a_list=arr
    return a_list