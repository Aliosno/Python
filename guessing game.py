my_name = "Nasty"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != my_name and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Guess my name: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You LOSE!")
else:
    print("Yes! You are right!")