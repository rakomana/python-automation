import alphabets

alphaObject= alphabets.Alphabet()

def game():
    direction = input("Do you want to encrypt or decrypt reply by (1 or 0) 0-decrypt 1-encrypt : ")
    message = input("Enter you message : ")
    encryption_level = input("Enter level of encryption from 1-3 : ")

    if direction == '1':
        encrypt(message, encryption_level)
    else:
        decrypt(message, encryption_level)

def encrypt(message, level):
    encoded = ''

    for letter in message:
        if letter == " ":
            encoded += " "
        else:
            position = alphaObject.words.index(letter)
            encoded += alphaObject.words[position + int(level)]
        
    print(f'encrypted word is {encoded}')

def decrypt(message, level):
    decoded = ''
    for letter in message:
        if letter == " ":
            decoded += " "
        else:
            position = alphabets.Alphabet().words.index(letter)
            decoded += alphabets.Alphabet().words[position - int(level)]

    print(f'decrypted word is {decoded}')

encryption = True

while encryption:
    game()