# Function to encrypt the message
def encrypt_caesar(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


# Function to decrypt the message (just reverses encryption)
def decrypt_caesar(encrypted_text, shift):
    return encrypt_caesar(encrypted_text, -shift)


# Main function to run the program
def main():
    print("Caesar Cipher Program")

    while True:
        print("\nOptions:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (integer): "))
            encrypted_message = encrypt_caesar(message, shift)
            print(f"Encrypted message: {encrypted_message}")

        elif choice == '2':
            encrypted_message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value (integer): "))
            decrypted_message = decrypt_caesar(encrypted_message, shift)
            print(f"Decrypted message: {decrypted_message}")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid option, please choose 1, 2, or 3.")


# Entry point of the program
if __name__ == "__main__":
    main()
