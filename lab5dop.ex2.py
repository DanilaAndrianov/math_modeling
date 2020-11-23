from sympy import symbols
from sympy.vector import CoordSys3D
from sympy import solve
N = CoordSys3D('N')
x = symbols('x')

a = 7*N.i + 2*N.j - 8*N.k
b = -4*N.i + x*N.j + 9*N.k
t=a.dot(b)

print(solve(t,x))