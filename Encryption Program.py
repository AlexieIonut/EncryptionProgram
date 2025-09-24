import random
import string

chars = string.punctuation + string.digits + string.ascii_letters + " "
chars = list(chars)
key = chars.copy()
random.shuffle(key)

def encrypt():
    plain_text = input('Enter a message to encrypt: ')
    cipher_text = ''

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]
    return ('Original message: {}\n'
            'Encryption message: {}'.format(plain_text,cipher_text))

def decrypt():
    cipher_text = input('Enter a message to decrypt: ')
    plain_text = ''

    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]
    return plain_text

def invalid_input(var):
    while var.lower() != 'e' and var.lower() != 'd':
        print('Invalid input')
        var = input('Do you want to encrypt or decrypt a message: (e/d) ?')

def main():
    print(encrypt())
    running = True
    while running:
        user_input = input("Do you want to encrypt or decrypt a message: (e/d)?\n"
                           "or press 'q' to quit: ")
        if user_input.lower() == 'e':
            print(encrypt())
        elif user_input.lower() == 'd':
            print(decrypt())
        elif user_input.lower() == 'q':
            break
        else:
            invalid_input(user_input)

if __name__ == "__main__":
    main()