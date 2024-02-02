def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

# Example usage:
text_to_encrypt = "Hello, World!"
shift_value = 3
encrypted_text = caesar_cipher(text_to_encrypt, shift_value)
print("Encrypted:", encrypted_text)

# To decrypt, use the same function with a negative shift value:
decrypted_text = caesar_cipher(encrypted_text, -shift_value)
print("Decrypted:", decrypted_text)
