def encrypt_vigenere(plaintext: list, keyword: list) -> str:

    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    keyword *= len(plaintext) // len(keyword) + 1
    ciphertext = ''
    for i, j in enumerate(plaintext):
        g = ord(j) + ord(keyword[i])
        ciphertext += chr(g%26 + ord('A'))
    ciphertext = str(ciphertext)

    return ciphertext


print(encrypt_vigenere(input(), input()))


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    # PUT YOUR CODE HERE
    return plaintext
    """