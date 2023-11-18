# To use bigger numbers than 10^4300, we need to set the max number of digits to 0
import sys
sys.set_int_max_str_digits(0)

# Read the file
with open('very_big_picture.png', 'rb') as f:
	data = f.read()

# Find all the primes in the file. A prime starts with 0x703d and ends with 0x2e
primes = []
for i in range(len(data)):
	if data[i] == 0x70 and data[i+1] == 0x3d:
		prime = []
		for j in range(i+2, len(data)):
			if data[j] == 0x2e:
				primes.append(int(''.join(prime)))
				break
			prime.append(chr(data[j]))

print(f"Found {len(primes)} primes")
for i, prime in enumerate(primes):
	print(f"p{i} = {prime}")

# Find the chiper text. The chiper text starts with 0x433d and ends with the file
for i in range(len(data)):
	if data[i] == 0x43 and data[i+1] == 0x3d:
		chiper = []
		for j in range(i+2, len(data)):
			chiper.append(chr(data[j]))

		break

chiper = ''.join(chiper)
chiper = int(chiper)
print(f"chiper = {chiper}")

# Write the primes to a file
with open('primes.txt', 'w') as f:
	for prime in primes:
		f.write(str(prime) + '\n')

# Write the chiper text to a file
with open('chiper.txt', 'w') as f:
	f.write(str(chiper) + '\n')
