import random

def choose_word():
      words = ["python", "hangman", "programming", "faizal", "artificial", "hackclub"]
      return random.choice(words)

def display_board(hidden_word, guessed_letters):
      display = ""
      for letter in hidden_word:
          if letter in guessed_letters:
              display += letter + " "
          else:
              display += "_ "
      print(display.strip())

def hangman():
      word_to_guess = choose_word()
      guessed_letters = set()
      attempts = 6

      print("Welcome to Hangman!")
      print("You have 6 attempts to guess the word.")

      while attempts > 0:
          display_board(word_to_guess, guessed_letters)
          guess = input("Guess a letter: ").lower()

          if guess in guessed_letters:
              print("You already guessed that letter. Try again.")
              continue

          guessed_letters.add(guess)

          if guess in word_to_guess:
              print(f"Good job! '{guess}' is in the word.")
          else:
              attempts -= 1
              print(f"Sorry, '{guess}' is not in the word. You have {attempts} attempts left.")

          if all(letter in guessed_letters for letter in word_to_guess):
              print(f"Congratulations! You guessed the word '{word_to_guess}'.")
              break
      else:
          print(f"Game over! The word was '{word_to_guess}'.")

if __name__ == "__main__":
     hangman()
