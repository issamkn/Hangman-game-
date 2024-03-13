import random
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for letter in chosen_word:
  display += "_"

lives = 6
end_of_game = False
while not end_of_game:


  guess = input("Guess a letter: ").lower()
  if guess in display:
    print(f"You have already guessed {guess}")

  n = -1
  for letter in chosen_word:
    n += 1
    if letter == guess:
      display[n] = guess
  print(f"{' '.join(display)}")
  
  if guess not in chosen_word:
    print("You guessed a wrong letter, you lose a life")
    lives -=1
    print(stages[lives])


  if lives > 0:
    if "_" not in display:
      end_of_game = True
      print("You win")
  else:
    end_of_game = True
    print("You lose")
