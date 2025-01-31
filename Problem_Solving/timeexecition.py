import time
def fun():
    st=time.time()
    s=0
    for i in range (1,n+1):
        s=s+i
    et=time.time()
    return s,et-st
n =4
print(fun())