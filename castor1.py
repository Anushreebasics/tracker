import matplotlib.pyplot as pl
import numpy as np
a=int(input("enter the number of subjects"))
b=1
d=[]
while(b<=a):
    c=input("enter the name of subject")
    d.append(c)
    b=b+1
n=int(input("enter the number of tests"))
n1=np.arange(n)
p={}

for i in d:
    s=[]
    m=1
    while(m<=n):
        print("enter the marks for test",m,"for",i)
        l=int(input())
        
        p[i]=s
        s.append(l)
        m=m+1
l=1
for i in p:
    pl.bar(n1+(0.2*l),p[i],width=0.2,label=i)
    pl.legend()
    l=l+1
    
    

