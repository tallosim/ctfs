import sys
sys.set_int_max_str_digits(0)

with open("level2.txt", "r") as f:
    lines = f.readlines()

n = int(lines[1].split('=')[1])
ct = int(lines[0].split('=')[1])

print(f"n: {n}")
print(f"ct: {ct}")

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def rsa_decrypt(c, d, n):
    m = pow(c, d, n)
    return m


phi = n - 1
e = 65537  # Public exponent

d = modinv(e, phi)
plaintext = rsa_decrypt(ct, d, n)

def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

plaintext = int_to_bytes(plaintext)

print("Decrypted message:", plaintext)
