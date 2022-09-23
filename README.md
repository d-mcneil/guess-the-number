# guess-the-number

# future improvements

- clean up return statements
- clean up variables that mirror variables in outer scope
- allow for more flexibility with user input
  - instead of doing == yes/no, too big/too small, first/second
    - something like if 'y' in response and 'n' not in response, or if 'fi' in response and 'se' not in response
    - check generate_user_feedback function in computer_guesses_game for an example of this
- consider just setting a quantity for max guesses and max number for each difficulty instead of giving option
- add medium difficulty

- difficulty levels
  - human guesses
    - hard - no help
    - medium - perhaps computer restates all previous guesses in list, but doesn't give range of possible numbers
    - easy - restates previous guesses if guessed again, and gives range of possible numbers as prompt for guess
  - computer guesses
    - hard - always guesses in the middle of the range
      - if max number is 500, computer will always be right on 9 (i think), so recommended guesses is 8
      - if max number is 1000, computer will always be right on 10 (i think), so recommended guesses is 9
      - if max number is 2000, computer will always be right on 11 (i think), so recommended guesses is 10
    - medium - perhaps making a smaller range and then guessing a random number within that range
    - easy - randomly guesses a number in the range of possible numbers
