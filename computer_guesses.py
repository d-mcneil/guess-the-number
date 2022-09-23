import random


def run_computer_guesses_game(difficulty, maximum_number, maximum_guesses):
    # if just this half of the game is run (i.e., only the computer guesses),
    # then these functions can be used to get maximum guesses and maximum number
    #
    # def get_maximum_number_user_input():
    #     maximum_number_user_input = input('Your number is between 1 and what whole number? ').strip()
    #     while not maximum_number_user_input.isnumeric() or maximum_number_user_input == '0':
    #         maximum_number_user_input = input('I\'m sorry, but to play this game, you need to enter a '
    #                                           'positive number with no decimal points. '
    #                                           'Your number is between 1 and what whole number? ').strip()
    #     maximum_number = int(maximum_number_user_input)
    #     return maximum_number
    #
    # def get_maximum_guesses_user_input():
    #     maximum_guesses_user_input = input('How many guesses will you give me? ').strip()
    #     while not maximum_guesses_user_input.isnumeric() or maximum_guesses_user_input == '0':
    #         maximum_guesses_user_input = input('I\'m sorry, but to play this game, you need to enter a '
    #                                            'positive number with no decimal points. '
    #                                            'How many guesses will you give me? ').strip()
    #     maximum_guesses = int(maximum_guesses_user_input)
    #     return maximum_guesses

    def ask_if_ready(minimum_number, maximum_number):
        print('\n', end='')
        while True:
            ready = input(f'When you\'ve thought of a number between {minimum_number} and '
                          f'{maximum_number} , please tell me "ready": ')
            if ready == 'ready':
                break

    def check_answer_obvious(minimum_number, maximum_number):
        answer_obvious = False
        if minimum_number == maximum_number:
            answer_obvious = True
        return answer_obvious

    def state_possible_range(guess_count, answer_obvious, minimum_number, maximum_number):
        if guess_count != 1 and not answer_obvious:
            if maximum_number - minimum_number == 1:
                print(f'Okay, so your number is either {minimum_number} or {maximum_number}.')
            else:
                print(f'Okay, so your number is between {minimum_number} and {maximum_number}.')

    def identify_which_guess_it_is(maximum_guesses, guess_count):
        if maximum_guesses == 1:
            print(f'\n(Only Guess)', end='')
        elif guess_count == 1:
            print(f'\n(First Guess)', end='')
        elif guess_count == maximum_guesses:
            print(f'\n(Final Guess)', end='')
        else:
            print(f'\n(Guess #{guess_count})', end='')

    def generate_computer_guess(difficulty, minimum_number, maximum_number):
        if difficulty == 'easy':
            computer_guess = random.randint(minimum_number, maximum_number)
        elif difficulty == 'hard':
            computer_guess = round((maximum_number + minimum_number) / 2)
        return computer_guess

    def state_guess(answer_obvious, computer_guess):
        if answer_obvious:
            print(f' Your number has to be {computer_guess}.')
        else:
            print(f' My guess is {computer_guess}.', end='')

    def check_correct(answer_obvious, computer_guess):
        if answer_obvious:
            correct = True
            return correct
        user_response = input(' Am I correct? ').strip().lower()
        while user_response != 'yes' and user_response != 'no':
            user_response = input(f'I don\'t understand. My guess was {computer_guess}. '
                                  f'Was I correct? Please tell me \"yes\" or \"no\": ').strip().lower()
        if user_response == 'yes':
            correct = True
        else:
            correct = False
        return correct

    def check_out_of_guesses(guess_count, maximum_guesses):
        out_of_guesses = False
        if guess_count == maximum_guesses:
            out_of_guesses = True
        return out_of_guesses

    def generate_user_feedback(computer_guess, minimum_number, maximum_number):
        if computer_guess == minimum_number:
            feedback = 'too small'
        elif computer_guess == maximum_number:
            feedback = 'too big'
        else:
            feedback = input('Was my guess too big or too small? ').strip().lower()
            while True:
                if 'bi' in feedback and 'sm' not in feedback:
                    feedback = 'too big'
                elif 'sm' in feedback and 'bi' not in feedback:
                    feedback = 'too small'
                if feedback != 'too big' and feedback != 'too small':
                    feedback = input(f'I don\'t understand. My guess was {computer_guess}. '
                                     f'Was my guess too big or too small? '
                                     f'Please tell me \"too big\" or \"too small\": ').strip().lower()
                else:
                    break
        return feedback

    def generate_new_maximum_number(computer_guess):
        return computer_guess - 1

    def generate_new_minimum_number(computer_guess):
        return computer_guess + 1

    def state_result(correct):
        if correct:
            print('\nHaha! You lose!')
        else:
            print('\nYou got me! You win!')

    correct, out_of_guesses = False, False
    guess_count = 0
    minimum_number = 1
    # if just this half of the game is run (i.e., only the human guesses),
    # then these variables can be used to store maximum guesses and maximum number
    #   maximum_number = get_maximum_number_user_input()
    #   maximum_guesses = get_maximum_guesses_user_input()
    maximum_number = maximum_number
    maximum_guesses = maximum_guesses
    difficulty = difficulty

    ask_if_ready(minimum_number, maximum_number)
    while not correct and not out_of_guesses:
        guess_count += 1
        answer_obvious = check_answer_obvious(minimum_number, maximum_number)
        state_possible_range(guess_count, answer_obvious, minimum_number, maximum_number)
        identify_which_guess_it_is(maximum_guesses, guess_count)
        computer_guess = generate_computer_guess(difficulty, minimum_number, maximum_number)
        state_guess(answer_obvious, computer_guess)
        correct = check_correct(answer_obvious, computer_guess)
        out_of_guesses = check_out_of_guesses(guess_count, maximum_guesses)
        if not correct and not out_of_guesses:
            feedback = generate_user_feedback(computer_guess, minimum_number, maximum_number)
            if feedback == 'too big':
                maximum_number = generate_new_maximum_number(computer_guess)
            elif feedback == 'too small':
                minimum_number = generate_new_minimum_number(computer_guess)
    state_result(correct)
    if correct:
        human_win = False
    else:
        human_win = True
    return human_win


if __name__ == '__main__':
    run_computer_guesses_game('hard', 2000, 10)
    # run_computer_guesses_game('easy', 250, 10)
