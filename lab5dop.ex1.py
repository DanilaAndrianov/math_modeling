from math import degrees
from sympy import symbols
from sympy.vector import CoordSys3D
from sympy import sin, cos, acos, trigsimp

x = CoordSys3D('x')
a, b, c = symbols('a, b, c')
a = 4*x.i + 3*x.j + 8*x.k
b = -2*x.i + 8*x.j + 7*x.k
c = -5*x.i - 6*x.j + 12*x.k

d=a.dot(b)
l=a.dot(c)
n=b.dot(c)
 
a1=a.magnitude()
b1=b.magnitude()
c1=c.magnitude()

u=d/(a1*b1)
u1=acos(u)

q=l/(a1*c1)
q1=acos(q)

p=n/(b1*c1)
p1=acos(p)

print(degrees(u1.evalf()))
print(degrees(q1.evalf()))
print(degrees(p1.evalf()))





