#!/usr/bin/env python
# coding: utf-8

# # Encryption mini project

# ##### Made by Pablo Gonzalez

# In[51]:


import math
import string

class Keypair:
    def __init__(self, p, q):
        e = None
        n = p*q
        phi_n = (p-1)*(q-1)
        for i in range(2, phi_n):
            if math.gcd(i, phi_n) == 1:
                e = i
                break
        self.public_key = (n, e)
        self.private_key = int((2*phi_n + 1)/e)

def encrypt(word, n, e):
    letter_list = []
    for i in list(word):
        letter_list.append(string.ascii_lowercase.index(i)+1)
    encryption = []
    for i in letter_list:
        encryption.append(int(math.pow(i, e)%n))
    return encryption

def decrypt(encryption, d, n):
    decryption = []
    for i in encryption:
        letter = int(pow(i, d)%n)
        decryption.append(string.ascii_lowercase[letter-1])
    return ''.join(decryption)


# In[66]:


# We create a keypair with a public key and a private key, given a pair of prime numbers.
keypair = Keypair(13, 17)

word = "pablogonzalezbaron"
print("Original word:", word)

# We encrypt the word 
encrypted_word = cipher(word, keypair.public_key[0], keypair.public_key[1])

print("Encrypted word:", encrypted_word)

# We decrypt the code 'encrypted_word' to show again the word
decrypted_word = decrypt(encrypted_word, keypair.private_key, keypair.public_key[0])

print("Decrypted word:", decrypted_word)

