import math
def check_snt(n):
    if n<=1:
        return False
    elif n<=3:
        return True
    elif n%2==0 or n%3==0:
        return False
    i =5 
    while i<= math.sqrt(n):
        if n%i==0 or n%(i+2)==0:
            return False
        i = i+6
    return True

def find(a,b,c,m,l):
    for i in range(m,l+1):
        if(check_snt(a*pow(i,2)+b*i+c)==True):
            print(i)

find(2,3,4,0,20)