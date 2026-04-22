#!/usr/bin/env python
# coding: utf-8

# # CRYPTOGRAPHY TOOL (Caeser and XOR)

# In[ ]:


def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def xor_encrypt(text, key):
    result = ""
    for char in text:
        result += chr(ord(char) ^ key)
    return result

def xor_decrypt(text, key):
    return xor_encrypt(text, key)


while True:
    print("\n===== 🔐 Cryptography Tool =====")
    print("1. Caesar Encrypt/Decrypt")
    print("2. XOR Encrypt/Decrypt")
    print("3. Combined (Caesar + XOR)")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        text = input("Enter text: ")
        shift = int(input("Enter shift value: "))

        encrypted = caesar_encrypt(text, shift)
        decrypted = caesar_decrypt(encrypted, shift)

        print("Encrypted (Caesar):", encrypted)
        print("Decrypted (Caesar):", decrypted)

    elif choice == '2':
        text = input("Enter text: ")
        key = int(input("Enter XOR key: "))

        encrypted = xor_encrypt(text, key)
        decrypted = xor_decrypt(encrypted, key)

        print("Encrypted (XOR):", encrypted)
        print("Decrypted (XOR):", decrypted)

    elif choice == '3':
        text = input("Enter text: ")
        shift = int(input("Enter shift value: "))
        key = int(input("Enter XOR key: "))

        # 🔐 Encryption
        step1 = caesar_encrypt(text, shift)
        final_encrypted = xor_encrypt(step1, key)

        # 🔓 Decryption
        step2 = xor_decrypt(final_encrypted, key)
        final_decrypted = caesar_decrypt(step2, shift)

        print("Encrypted (Caesar + XOR):", final_encrypted)
        print("Decrypted back:", final_decrypted)

    elif choice == '4':
        print("Program Closed ✅")
        break

    else:
        print("Invalid choice ❌ Try again!")


# In[ ]:




