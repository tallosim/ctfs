from Crypto.Util.number import isPrime, getRandomNBitInteger, bytes_to_long

flag = b"HKN{REDACTED}"

def pub_key(key_len: int) -> int:
    while True:
        x = getRandomNBitInteger(key_len)
        p = x**6 + 2*x**5 + 4*x**4 - 9*x**3 - x**2 + 20*x + 3141592
        q = 2*x**5 + 7*x**4 - 14*x**3 + 9*x**2 + 2718281

        if isPrime(p) and isPrime(q):
            return p * q

def enc(pt: bytes, n: int, e: int) -> int:
	m = bytes_to_long(pt)
	return pow(m, e, n)

n = pub_key(64)
ct = enc(flag, n, 65537)

with open("output.txt", "w") as f:
     f.write(f"n = {n}\n")
     f.write(f"enc = {ct}")