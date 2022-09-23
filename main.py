import random


def guess_the_secret_number_game():
    from human_guesses import run_human_guesses_game
    from computer_guesses import run_computer_guesses_game

    def get_difficulty():
        difficulty = input('What difficulty do you want to play at? Easy or hard? ').strip().lower()
        while difficulty != 'hard' and difficulty != 'easy':
            difficulty = input(f'I don\'t understand. What difficulty do you want to play at? '
                               f'Please tell me \"easy\" or \"hard\": ').strip().lower()
        return difficulty

    def get_maximum_number(difficulty):
        if difficulty == 'easy':
            print('The recommended highest possible number for "easy" is 250.', end=' ')
        elif difficulty == 'hard':
            print('The recommended highest possible number for "hard" is 2000.', end=' ')
        maximum_number_user_input = input('What do you want the highest possible number to be? ').strip()
        while not maximum_number_user_input.isnumeric() or maximum_number_user_input == '0':
            maximum_number_user_input = input('I\'m sorry, but to play this game, you need to enter a '
                                              'positive number with no decimal points. '
                                              'What do you want the highest possible number to be? ').strip()
        return int(maximum_number_user_input)

    def get_maximum_guesses():
        print('The recommended amount of guesses per round is 10.', end=' ')
        maximum_guesses_user_input = input('How many guesses do you want each of us to have? ').strip()
        while not maximum_guesses_user_input.isnumeric() or maximum_guesses_user_input == '0':
            maximum_guesses_user_input = input('I\'m sorry, but to play this game, you need to enter a '
                                               'positive number with no decimal points. '
                                               'How many guesses do you want each of us to have? ').strip()
        return int(maximum_guesses_user_input)

    def coin_flip():
        def who_guesses_first():
            user_input_guess_first_or_second = input('Do you want to be the guesser first or second? ').strip().lower()
            while user_input_guess_first_or_second != 'first' and user_input_guess_first_or_second != 'second':
                user_input_guess_first_or_second = input(f'I don\'t understand. Do you want to guess first or second? '
                                                         f'Please tell me \"first\" or \"second\": ').strip().lower()
            if user_input_guess_first_or_second == 'first':
                first_guesser = 'human'
            else:
                first_guesser = 'computer'
            return first_guesser

        call = input('Let\'s flip a coin to see goes first. Call heads or tails: ').strip().lower()
        while call != 'heads' and call != 'tails':
            call = input('Please call either "heads" or "tails": ').strip().lower()
        coin_flip = random.choice(['heads', 'tails'])
        print(f'\nThe coin landed on {coin_flip}. ', end='')
        if call == coin_flip:
            print('You won the toss, so you get to choose.')
            first_guesser = who_guesses_first()
        else:
            print('I won the toss, so I will guess first.')
            first_guesser = 'computer'
        return first_guesser

    def scoreboard(game_count, guesser, win_count, loss_count):
        print(f"\n\nGame {game_count}")
        if game_count > 1:
            print(f'\nTotal Wins = {win_count}\nTotal Losses = {loss_count}\n')
            if guesser == 'human':
                print('It\'s your turn to guess.')
            else:
                print('It\'s my turn to guess.')

    def play_game(guesser, difficulty, maximum_number, maximum_guesses):
        if guesser == 'human':
            result = run_human_guesses_game(difficulty, maximum_number, maximum_guesses)
        else:
            result = run_computer_guesses_game(difficulty, maximum_number, maximum_guesses)
        return result

    def alternate_guesser(previous_guesser):
        if previous_guesser == 'human':
            new_guesser = 'computer'
        else:
            new_guesser = 'human'
        return new_guesser

    def check_play_again():
        user_response_play_again = input("Do you want to play again? ").strip().lower()
        while user_response_play_again != 'yes' and user_response_play_again != 'no':
            user_response_play_again = input(f'I don\'t understand. Do you want to play again? '
                                             f'Please tell me \"yes\" or \"no\": ').strip().lower()
        if user_response_play_again == 'yes':
            play_again = True
        else:
            play_again = False
        return play_again

    print("\n\"Guess the Secret Number: Human vs. Computer\" - written by Dean McNeil\n")
    play_again, game_count, win_count, loss_count = True, 0, 0, 0
    difficulty = get_difficulty()
    maximum_number = get_maximum_number(difficulty)
    maximum_guesses = get_maximum_guesses()
    guesser = coin_flip()

    while play_again:
        game_count += 1
        scoreboard(game_count, guesser, win_count, loss_count)
        human_win = play_game(guesser, difficulty, maximum_number, maximum_guesses)
        if human_win:
            win_count += 1
        else:
            loss_count += 1
        play_again = check_play_again()
        if play_again:
            guesser = alternate_guesser(guesser)
    print(f"\n\nThank you for playing!\nTotal Wins = {win_count}\nTotal Losses = {loss_count}")


if __name__ == '__main__':
    guess_the_secret_number_game()
