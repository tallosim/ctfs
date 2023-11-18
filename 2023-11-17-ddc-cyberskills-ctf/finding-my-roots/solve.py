with open("output.txt", "r") as f:
    lines = f.readlines()

n = int(lines[0].split('=')[1])

from sympy import symbols, Eq, solve

def solve_system_of_equations(n):
    x = symbols('x')

    # Expressions for p and q
    p = x**6 + 2*x**5 + 4*x**4 - 9*x**3 - x**2 + 20*x + 3141592
    q = 2*x**5 + 7*x**4 - 14*x**3 + 9*x**2 + 2718281

    # Equation for n = pq
    equation = Eq(p * q, n)

    # Solve the equation for x
    solutions = solve(equation, x)

    if not solutions:
        print("No solutions found.")
        return None

    # Choose one solution (you may need to check which solution is correct in your context)
    x_value = solutions[0]

    # Calculate p and q using the chosen x value
    p_value = p.subs(x, x_value)
    q_value = q.subs(x, x_value)

    return p_value, q_value

# Extract p and q from the system of equations
p, q = solve_system_of_equations(n)

print(f"p = {p}")
print(f"q = {q}")
