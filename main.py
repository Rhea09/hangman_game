from random import choice


def run_game():
    word: str = choice(['apple', 'secret', 'banana', 'reckless', 'squash', 'temptation', 'crown'])
    username: str = input('What is your name? >>')
    print(f'Welcome to hangman, {username}')

    # setup
    guessed: str = ''
    tries: int = 3

    while tries > 0:
        blanks: int = 0

        print('Word: ', end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks += 1

        print()  # adds a blank line

        if blanks == 0:
            print('You got it')
            break

        guess: str = input('Enter a letter: ')
        if len(guess) > 20:
            print('Only guess single letters or the final word')
        if guess in guessed:
            print(f'You already tried: "{guess}". Please try with another letter!')
            continue

        guessed += guess

        if guess not in word:
            tries -=1
            print(f'sorry that was wrong :( ... {tries} tries remaining')
            if tries == 0:
                print('Game over. You lose')
                break


if __name__ == "__main__":
    run_game()
