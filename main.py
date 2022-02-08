#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
count=random.randint(0,len(word_list)-1)
chosen_word=word_list[count]
chosen_word=list(chosen_word)
guess_flag=True
while(guess_flag):
  guess=input("Guess a letter : ").lower()
  for i in chosen_word:
    if i==guess:
      print("Right")
    else:
      print("Wrong")
  guess_flag=False