import random

def game():
    words = ['eating', 'drinking', 'praying']

    word = random.choice(words)
    live = 6

    print(f'The solution is {word}')

    display = []

    for letter in word:
        display += "_"

    print(f'{display}')

    end_loop = False

    while not end_loop:    
        value = input('Guess a letter : ')

        for pos in range(len(word)):
            letter = word[pos]
            
            if letter == value:
                display[pos] = value
            else:
                live = live - 1

        if value not in word:
            live = live - 1
            print(f'You lost')

        print(f'You have {live} lives')
        print(f'{display}')

        if "_" not in display:
            end_loop = True
            print(f'You won')


game()

