import random


def run_human_guesses_game(difficulty, maximum_number, maximum_guesses):
    # if just this half of the game is run (i.e., only the human guesses),
    # then these functions can be used to get maximum guesses and maximum number
    #
    # def get_maximum_number_user_input():
    #     maximum_number_user_input = input('What do you want the highest possible number to be? ').strip()
    #     while not maximum_number_user_input.isnumeric() or maximum_number_user_input == '0':
    #         maximum_number_user_input = input('I\'m sorry, but to play this game, you need to enter a '
    #                                           'positive number with no decimal points. '
    #                                           'What do you want the highest possible number to be? ').strip()
    #     maximum_number = int(maximum_number_user_input)
    #     return maximum_number
    #
    # def get_maximum_guesses_user_input():
    #     maximum_guesses_user_input = input('How many guesses do you want? ').strip()
    #     while not maximum_guesses_user_input.isnumeric() or maximum_guesses_user_input == '0':
    #         maximum_guesses_user_input = input('I\'m sorry, but to play this game, you need to enter a '
    #                                            'positive number with no decimal points. '
    #                                            'How many guesses do you want? ').strip()
    #     maximum_guesses = int(maximum_guesses_user_input)
    #     return maximum_guesses

    def identify_which_guess_it_is(maximum_guesses, guess_count):
        if maximum_guesses == 1:
            print(f'\n(Only Guess) ', end='')
        elif guess_count == 1:
            print(f'\n(First Guess) ', end='')
        elif guess_count == maximum_guesses:
            print(f'\n\n(Final Guess) ', end='')
        else:
            print(f'\n\n(Guess #{guess_count}) ', end='')

    def generate_new_maximum_number(user_guess):
        return user_guess - 1

    def generate_new_minimum_number(user_guess):
        return user_guess + 1

    def get_user_guess(guess_count, maximum_number, difficulty, minimum_number, feedback, previous_guesses):
        def get_user_guess_input(guess_count, maximum_number, difficulty, minimum_number, feedback):
            if guess_count == 1:
                user_guess_input = input(f"Guess a whole number from 1 to {maximum_number}: ").strip()
            elif difficulty == 'easy':
                if maximum_number == minimum_number:
                    user_guess_input = input(f"The number has to be {maximum_number}. Guess the number: ").strip()
                else:
                    user_guess_input = input(f"The number has to be between {minimum_number} and {maximum_number}. "
                                             f"Guess another number: ").strip()
            else:
                if feedback == 'too big':
                    user_guess_input = input("Guess a smaller number: ").strip()
                else:
                    user_guess_input = input("Guess a bigger number: ").strip()
            return user_guess_input

        while True:
            user_guess_input = get_user_guess_input(guess_count, maximum_number, difficulty, minimum_number, feedback)
            if not user_guess_input.isnumeric() or user_guess_input == '0':
                print('I\'m sorry, but to play this game, you need to enter a positive number with no decimal points. ',
                      end='')
            else:
                user_guess = int(user_guess_input)
                if difficulty == 'easy':
                    if user_guess in previous_guesses:
                        print('You\'ve already guessed that number. ', end='')
                    elif user_guess > maximum_number or user_guess < minimum_number:
                        print('That number is outside the range of possible correct answers. ', end='')
                    else:
                        break
                else:
                    break
        return user_guess

    def check_correct(user_guess, number_to_guess):
        if user_guess == number_to_guess:
            correct = True
        else:
            correct = False
        return correct

    def check_out_of_guesses(guess_count, maximum_guesses):
        out_of_guesses = False
        if guess_count == maximum_guesses:
            out_of_guesses = True
        return out_of_guesses

    def generate_computer_feedback(user_guess, number_to_guess):
        if user_guess > number_to_guess:
            print('Incorrect! Your number is too big.', end='')
            feedback = 'too big'
        elif user_guess < number_to_guess:
            print('Incorrect! Your number is too small.', end='')
            feedback = 'too small'
        else:
            print(f'Correct! You guessed it!', end='')
            feedback = ''
        return feedback

    def state_result(number_to_guess, correct):
        print(f' The number was {number_to_guess}.')
        if correct:
            print('\nYou got me! You win!')
        else:
            print('\nHaha! You lose!')

    correct, out_of_guesses = False, False
    guess_count, feedback, previous_guesses = 0, '', []
    # if just this half of the game is run (i.e., only the human guesses),
    # then these variables can be used to store maximum guesses and maximum number
    #   maximum_number = get_maximum_number_user_input()
    #   maximum_guesses = get_maximum_guesses_user_input()
    minimum_number = 1
    number_to_guess = random.randint(minimum_number, maximum_number)


    while not correct and not out_of_guesses:
        guess_count += 1
        identify_which_guess_it_is(maximum_guesses, guess_count)
        user_guess = get_user_guess(guess_count, maximum_number, difficulty, minimum_number, feedback, previous_guesses)
        feedback = generate_computer_feedback(user_guess, number_to_guess)
        correct = check_correct(user_guess, number_to_guess)
        out_of_guesses = check_out_of_guesses(guess_count, maximum_guesses)
        if difficulty == 'easy' and not out_of_guesses:
            previous_guesses.append(user_guess)
            if number_to_guess < user_guess <= maximum_number:
                maximum_number = generate_new_maximum_number(user_guess)
            elif number_to_guess > user_guess >= minimum_number:
                minimum_number = generate_new_minimum_number(user_guess)
    state_result(number_to_guess, correct)
    if correct:
        human_win = True
    else:
        human_win = False
    return human_win


if __name__ == '__main__':
    run_human_guesses_game('hard', 2000, 10)
    # run_human_guesses_game('easy', 250, 10)
