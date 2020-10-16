#Num.py
def num(n):
    sum=0
    for i in list(str(n)):
        sum+=int(i)**4
    if sum==n:
        return True
    else:
        return False
    
for i in range(1000,10000):
    if num(i):
        print(i)
