
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build an interactive Hangman game in Python that uses user input, string handling, loops, and conditional logic.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Create a list of possible secret words, select one at random, and initialize the game state.

#### Requirements
Completed program should:

- Use a predefined list of words
- Randomly choose the secret word for each game
- Initialize variables for guessed letters, incorrect guesses, and maximum attempts

### 🛠️ Guess Input and Progress Display

#### Description
Accept letter guesses from the player, reveal matched letters in the hidden word, and show current progress.

#### Requirements
Completed program should:

- Prompt the player for a single letter guess
- Display the current word progress using blanks and revealed letters
- Track letters already guessed and avoid duplicate processing

### 🛠️ Win/Lose Conditions and Feedback

#### Description
End the game when the word is guessed or when the player runs out of attempts, then display the appropriate result.

#### Requirements
Completed program should:

- End when the full word is guessed
- End when incorrect guesses reach the maximum allowed
- Show a win message if the player guesses the word
- Show a lose message and reveal the correct word if attempts are exhausted
