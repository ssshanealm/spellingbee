from get_word import get_word                 
from score import get_point_value               

def spelling_bee():
  #Your code here
  print("Welcome to Spelling Bee!")  
  letters_input = input("Enter your 7 letters, separated by commas: ")
  letters = letters_input.split(",")  

  required_letter = input("Which of these 7 letters " + str(letters) + " will be your required letter? ").upper().strip()
  while required_letter not in letters:
    print(required_letter + " is not an available letter. Please choose from the following: " + str(letters))
    required_letter = input("Which of these 7 letters " + str(letters) + " will be your required letter? ").upper().strip()

  used_words = []
  total_score = 0

  while True:  
    word = get_word(letters, required_letter, used_words)

    if word == "END":  
      print("Your final score is " + str(total_score))
      break

    if word not in used_words:
      used_words.append(word)  
            
      points = get_point_value(word, letters)
      total_score += points  
    else:
      print("Already used.")

spelling_bee()  # DO NOT REMOVE
