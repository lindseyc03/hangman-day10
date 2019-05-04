random_word = 'code'
word = list(random_word)
blank = '_'
blanklist = list(blank)
blanklist *= len(word)

print(blanklist)
wrong_guess = 0
for i in range(0, len(word)):
  userguess = input("Enter a letter: ")
  if userguess in word:
    for index in range(len(word)):
      if userguess == word[index]:
        blanklist[index] = userguess 
    print("Good guess", blanklist)
  else:
    wrong_guess += 1
    print("You have", len(word) - wrong_guess, "tries left" )
