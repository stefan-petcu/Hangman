This is a simple Hangman game implemented in Python. The player must guess the letters of a hidden word within a limited number of attempts. The game provides feedback after each guess, displaying the correctly guessed letters and the remaining lives.

Features

Random word selection from a predefined list

Interactive guessing system

Limited number of incorrect attempts

Visual representation of progress

Text-based interface

Installation

Clone the repository:

git clone https://github.com/stefan-petcu/Hangman.git
cd Hangman

Ensure you have Python installed (Python 3 recommended).

Run the script:

python hangman.py

How to Play

The game selects a random word.

The player guesses one letter at a time.

If the letter is in the word, it is revealed in the correct position.

If the letter is not in the word, the player loses a life.

The game ends when the player correctly guesses the word or runs out of lives.

Example Gameplay

Welcome to Hangman!
Word: _ _ _ _ _
Guess a letter: e
Correct!
Word: _ e _ _ _
Guess a letter: x
Incorrect! You have 5 lives left.

Future Improvements

Add a graphical interface using Tkinter or Pygame

Implement a difficulty level selection

Fetch words from an external API

License

This project is open-source and available under the MIT License.

Author

Stefan Petcu

Feel free to contribute or suggest improvements! 🚀

