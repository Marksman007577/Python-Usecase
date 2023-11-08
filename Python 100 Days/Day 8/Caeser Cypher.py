from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift_number):
    """This function encrypts a word based on number of shift"""
    encrypted_word = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_number
        new_letter = alphabet[new_position]
        encrypted_word += new_letter
    return encrypted_word


def decrypt(encryption, shift_number):
    """This function decrypts an encrypted word based on number of shift"""
    decrypted_word = ""
    for letter in encryption:
        position = alphabet.index(letter)
        new_position = position - shift_number
        new_letter = alphabet[new_position]
        decrypted_word += new_letter
    return decrypted_word


print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

to_continue = True

while to_continue:
    if direction == 'encode'.lower():
        encryptedWord = encrypt(plain_text=text, shift_number=shift)
        print(f"encrypted word is: {encryptedWord}")
    else:
        decryptedWord = decrypt(encryption=text, shift_number=shift)
        print(f"decrypted word is: {decryptedWord}")

    question = input("Would you like to encode or decode? Type y for 'Yes' and n for 'No'.").lower()

    if question == 'n':
        print("Thank's for using our service")
        to_continue = False
