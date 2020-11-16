print('                  ~~~~~Guess any Number~~~~~~')
secret_number: int = 832
guess_count = 0
guess_limit = 3
guess = "   "
while guess_count < guess_limit and len(str(guess)) == 3:
    guess = int(input("Guess any number:"))
    guess_count += 1
    if guess == secret_number:
        print("""✔︎ You have WON! """)
        break
    else:
        if guess_limit - guess_count != 0:
         print(f"You have tries {guess_limit - guess_count} left")
else:
    print("number should be 3 digits long")
if guess_limit - guess_count == 0 and guess != secret_number:
    print("Game over")
