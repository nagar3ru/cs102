def encrypt_caesar(plaintext: str):

    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """

    ciphertext = [0] * len(plaintext)

    case = {
        'x': 'a',
        'y': 'b',
        'z': 'c',
        'X': 'A',
        'Y': 'B',
        'Z': 'C'
    }
    for t in range(len(plaintext)):
        ciphertext[t] = plaintext[t]
    for i in range(len(plaintext)):
        if 65 <= ord(plaintext[i]) <= 87 or 97 <= ord(plaintext[i]) <= 119:
            ciphertext[i] = chr(ord(plaintext[i])+ 3)
        elif 88 <= ord(plaintext[i]) <= 90 or 120 <= ord(plaintext[i]) <= 122:
            ciphertext[i] = case[plaintext[i]]
    ciphertext = ''.join(ciphertext)

    return ciphertext


print(encrypt_caesar(input()))



def decrypt_caesar(ciphertext: str):

    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """

    plaintext = [0] * len(ciphertext)

    case2 = {
        'a': 'x',
        'b': 'y',
        'c': 'z',
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    }
    for t in range(len(ciphertext)):
        plaintext[t] = ciphertext[t]
    for i in range(len(ciphertext)):
        if ord('D') <= ord(ciphertext[i]) <= ord('Z') or ord('d') <= ord(ciphertext[i]) <= ord('z'):
            plaintext[i] = chr(ord(ciphertext[i]) - 3)
        elif ord('a') <= ord(ciphertext[i]) <= ord('c') or ord('A') <= ord(ciphertext[i]) <= ord('C'):
            plaintext[i] = case2[ciphertext[i]]
    plaintext = ''.join(plaintext)

    return plaintext

print(decrypt_caesar(input()))
