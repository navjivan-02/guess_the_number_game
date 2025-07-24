from random import randint

def generate_random():
    return randint(1, 100)

def perfect_guess():
    print("========== THE PERFECT GUESS ==========")
    print("\n🎲 I have selected a number between 1 and 100.")

    computer_number = generate_random()
    guess_count = 0

    while True:
        try:
            user_guess = int(input("🤔  Can you guess it? :: "))
            guess_count += 1

            if user_guess == computer_number:
                print(f"\n🥳 Superb! You guessed it correctly in {guess_count} attempt(s).\n")
                break
            elif user_guess < computer_number:
                print("🔼  Try a higher number!\n")
            else:
                print("🔽  Try a lower number!\n")

        except ValueError:
            print("⚠️ Please enter a valid number.\n")

if __name__ == "__main__":
    perfect_guess()
