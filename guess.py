import random

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
            "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
            "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
            "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
            "51", "52", "53", "54", "55", "56", "57", "58", "59", "60",
            "61", "62", "63", "64", "65", "66", "67", "68", "69", "70",
            "71", "72", "73", "74", "75", "76", "77", "78", "79", "80",
            "81", "82", "83", "84", "85", "86", "87", "88", "89", "90",
            "91", "92", "93", "94", "95", "96", "97", "98", "99", "100"]

LUCKY_NUMBER = random.choice(numbers)

level = input("Type 0 - for easy and Type 1 - for hard : ")

attempts = 10 if level == "1" else 5

print(f'You have {attempts} attempts')

attempts_status = True

while attempts_status:
    guess = input("Guess a number between (1 - 100) : ")

    if guess > LUCKY_NUMBER:
        print(f'Too high')
    elif guess < LUCKY_NUMBER:
        print(f'Too Low')
    else:
        attempts_status = False
        print(f'You won')

    attempts -= 1
    print(f'Attempts : {attempts}')

    if attempts == 0:
        print(f'You lost')
        attempts_status = False