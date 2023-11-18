# Finding my roots - Cryptography

This challenge was a easier RSA challange.

The challenge provided us with a [Python script](./chall.py) and a [output file](./output.txt). The script was used to generate the output file. The output file contained a modulus and a ciphertext.

From the provided script we can see that the modulus is the product of two primes, and the primes are created from the same `x` value with different functions. If we can find the `x` value, we can find the primes and decrypt the ciphertext.

I wrote a Python script to solve the system of equations for `x` and calculate the primes.

```python
#!/usr/bin/env python3

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
```

Now that we have the primes, we can decrypt the ciphertext.

```python
#!/usr/bin/env python3

with open("output.txt", "r") as f:
    lines = f.readlines()

n = int(lines[0].split('=')[1])
ct = int(lines[1].split('=')[1])
p = int(lines[2].split('=')[1])
q = int(lines[3].split('=')[1])

# Euler's totient function
phi = (p - 1) * (q - 1)

# Public exponent
e = 65537

# Private exponent
d = pow(e, -1, phi)

# Decrypt the ciphertext
m = pow(ct, d, n)

# Convert the plaintext to a string
m = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()
```

The decrypted message was the flag.

```txt
HKN{1_4m_r0071n6_f0r_y0u}
```
