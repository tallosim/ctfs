import sys
sys.set_int_max_str_digits(0)

primes = []
with open('primes.txt', 'r') as f:
    for line in f.readlines():
        primes.append(int(line.strip()))

chiper = 0
with open('chiper.txt', 'r') as f:
    chiper = int(f.readline().strip())


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

# Replace these values with your actual data
e = 65537  # public exponent
c = chiper  # ciphertext

# Calculate the modulus (n) from the prime numbers
n = 1
for prime in primes:
    n *= prime

# Calculate the private exponent (d)
phi = 1
for prime in primes:
    phi *= (prime - 1)

print(f"phi = {phi}")
d = modinv(e, phi)
print(f"d = {d}")

# Decrypt the ciphertext
plaintext = rsa_decrypt(c, d, n)

def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

plaintext = int_to_bytes(plaintext)

print("Decrypted message:", plaintext)
