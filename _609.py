from math import sqrt
PI=3.141592654
r,d=input('').split(" ")
r=float(r)
d=float(d)
h=r-d/2
a=sqrt(h*(2*r-h))
print(round(a*a*PI,2))

