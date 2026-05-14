 # 📘 Assignment: Hangman Game Challenge

 ## 🎯 Objective

 Build a command-line Hangman game in Python that exercises string manipulation, loops, conditionals, and random selection. Students will implement a playable game loop that accepts guesses and enforces a limit on incorrect attempts.

 ## 📝 Tasks

 ### 🛠️	Implement Hangman Game

 #### Description
 Create a Python program that:

 - Randomly chooses a secret word from a predefined list.
 - Displays the secret word progress using underscores for unknown letters (for example: `_ _ a _ _`).
 - Accepts single-letter guesses from the player and updates the display accordingly.
 - Tracks incorrect guesses and remaining attempts.
 - Ends the game when the word is fully guessed or when attempts are exhausted, showing a win or lose message.

 #### Requirements
 Completed program should:

 - Randomly select words from a predefined list.
 - Accept letter guesses and show current progress (e.g., `_ _ a _ _`).
 - Keep track of letters already guessed (both correct and incorrect).
 - Subtract from a fixed number of allowed incorrect attempts for wrong guesses.
 - End with a clear win or lose message; on loss, reveal the secret word.
 - Be runnable from the command line (for example: `python3 hangman.py`).

 #### Example
 A short example interaction:

 ```
 Welcome to Hangman!
 Word: _ _ _ _ _
 Guesses remaining: 6
 Guess a letter: a
 Good guess! Word: _ a _ _ _
 Guesses remaining: 6
 Guess a letter: z
 Wrong. Guesses remaining: 5
 ...
 You win! The word was: magic
 ```
