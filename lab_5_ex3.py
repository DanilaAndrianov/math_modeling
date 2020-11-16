
from sympy import symbols
from sympy import solve
x = symbols('x')
expr=x**2 + x + 1/x + 1/x**2 - 4
solve_expr=solve(expr,x)
print(solve_expr)









ε = 0.8
M = 9


