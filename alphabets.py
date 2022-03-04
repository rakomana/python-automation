import random

class Alphabet:
    words = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "?", "_", "-",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "/", "*", ",", "@",
    "#", "!", "%", "%", "^", ".", "=", "-", ")", "(", "{", "}", "[", "]"]

    def __init__(self):
        self.letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.mails = ["@gmail.com", "@yahoo.com", "@outlook.com"]

    def generate_email(self):
        email_address = ''
        for letter in range(10):
            email_address += random.choice(self.letters)

        return email_address + random.choice(self.mails)



