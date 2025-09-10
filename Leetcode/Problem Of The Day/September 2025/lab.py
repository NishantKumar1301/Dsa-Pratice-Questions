#Vernam Cypher
import random

def generate_key(n): # n = length of plain text
    key = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(n))
    return key

def encrypt(plaintext, key):
    cipher_bytes = bytes([ord(p) ^ ord(k) for p, k in zip(plaintext, key)])
    return cipher_bytes.hex() 

def decrypt(cipher_text, key):
    cipher_bytes = bytes.fromhex(cipher_text)
    decrypted_text = ''.join(chr(c ^ ord(k)) for c, k in zip(cipher_bytes, key))
    return decrypted_text

plaintext = "HELLO"
key = generate_key(len(plaintext))

print("Plaintext:", plaintext)
print("Key:", key)

cipher_text = encrypt(plaintext, key)
print("cipher_text:", cipher_text)

decrypted_text = decrypt(cipher_text, key)
print("Decrypted Text:", decrypted_text)

#Affine cipher 

print("---------------------------------------------------------------------------------")
# Implementation of Affine Cipher in Python

def egcd(a, b): #Extended eucledian geometry
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m): #Modular inverse
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  
    else:
        return x % m


def affine_encrypt(text, key):
    '''
    C = (a*P + b) % 26
    '''
    return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) 
                  + ord('A')) for t in text.upper().replace(' ', '') ])


def affine_decrypt(cipher, key):
    '''
    P = (a^-1 * (C - b)) % 26
    '''
    return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1])) 
                    % 26) + ord('A')) for c in cipher ])

text = 'AFFINE CIPHER'
key = [17, 20]
print(f"Original Text : {text} ")
affine_encrypted_text = affine_encrypt(text, key)

print('Encrypted Text: {}'.format( affine_encrypted_text ))

# calling decryption function
print('Decrypted Text: {}'.format
( affine_decrypt(affine_encrypted_text, key) ))