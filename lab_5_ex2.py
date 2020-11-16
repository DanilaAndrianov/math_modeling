import math
import sympy
from sympy import symbols
from sympy import sqrt, simplify

a = symbols('a')
simp_expr=sympy.simplify(sqrt(a)-a/sqrt(a)+1)*(a-1)/sqrt(a)
print(simp_expr)



