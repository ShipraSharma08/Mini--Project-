#!/usr/bin/env python
# coding: utf-8

# # Secure Message System using OTP(One Time Pad) & Fiestel Cipher

# In[ ]:


import random

# 🔐 One Time Pad
def generate_key(length):
    return ''.join(chr(random.randint(0, 255)) for _ in range(length))

def otp_encrypt(text, key):
    return ''.join(chr(ord(t) ^ ord(k)) for t, k in zip(text, key))

def otp_decrypt(cipher, key):
    return otp_encrypt(cipher, key)


# 🔐 Feistel Cipher
def feistel_round(left, right, key):
    new_left = right
    new_right = ''.join(chr(ord(l) ^ (ord(r) ^ key)) for l, r in zip(left, right))
    return new_left, new_right

def feistel_encrypt(text, rounds, key):
    if len(text) % 2 != 0:
        text += ' '  # padding

    half = len(text) // 2
    left = text[:half]
    right = text[half:]

    for _ in range(rounds):
        left, right = feistel_round(left, right, key)

    return left + right

def feistel_decrypt(cipher, rounds, key):
    half = len(cipher) // 2
    left = cipher[:half]
    right = cipher[half:]

    for _ in range(rounds):
        right, left = feistel_round(right, left, key)

    return left + right


# 🔁 MAIN PROGRAM
while True:
    print("\n==== 🔐 Secure Message System ====")
    print("1. One Time Pad")
    print("2. Feistel Cipher")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        text = input("Enter message: ")
        key = generate_key(len(text))

        enc = otp_encrypt(text, key)
        dec = otp_decrypt(enc, key)

        print("Key:", key)
        print("Encrypted:", enc)
        print("Decrypted:", dec)

    elif choice == '2':
        text = input("Enter message: ")
        rounds = int(input("Enter number of rounds: "))
        key = int(input("Enter key (number): "))

        enc = feistel_encrypt(text, rounds, key)
        dec = feistel_decrypt(enc, rounds, key)

        print("Encrypted:", enc)
        print("Decrypted:", dec)

    elif choice == '3':
        print("Program Ended ✅")
        break

    else:
        print("Invalid choice ❌")


# In[ ]:




