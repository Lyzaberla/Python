
secret_word = "Amomea"
guess_word = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess_word != secret_word and not out_of_guess:
    if guess_count < guess_limit:
      guess_word = input("Enter a guess word:")
      guess_count += 1
    else:
        out_of_guess = True
        
if out_of_guess:
    print("out of guess! you lose.")
else:
    print("Good job! you win.")


