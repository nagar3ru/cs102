import random

def is_prime(n: int) -> bool:
    """
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    divisor = 1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def generate_keypair(p: int, q: int) -> tuple:
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q

    phi = (p-1)*(q-1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

def gcd(a: int, b: int) -> int:
    """
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a

    return a + b

def multiplicative_inverse(e: int, phi: int) -> int:
    """
    >>> multiplicative_inverse(7, 40)
    23
    """
    v = []
    while True:
        v.append([phi, e, phi % e, phi // e])
        phi, e = e, v[-1][2]
        if v[-1][2] == 0:
            break
    v[-1].extend([0, 1])
    for i in range(len(v)-2, -1, -1):
        x = v[i+1][-1]
        y = v[i+1][-2] - v[i+1][-1] * v[i][3]
        v[i].extend([x, y])
    d = v[0][-1] % v[0][0]
    return d

def encrypt(pk: int, plaintext: str) -> list:
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher

def decrypt(pk: int, ciphertext: str) -> str:

    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(plain)

if __name__ == '__main__':
    p = int(input("Enter a prime number: "))
    q = int(input("Enter another prime number: "))
    public, private = generate_keypair(p, q)
    print('\n')
    print("Your public key is ", public)
    print("Your private key is ", private)
    print('\n')
    message = input("Enter a message to encrypt: ")
    encrypted = encrypt(private, message)
    print("Your encrypted message is: ")
    print(''.join(map(lambda x: str(x), encrypted)))
    print('\n')
    print("Decrypting message with public key ", public, ".")
    print("Your message is:")
    print(decrypt(public, encrypted))

