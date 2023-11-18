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

print(m)