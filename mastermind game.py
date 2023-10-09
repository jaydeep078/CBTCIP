import random

def generate_secret_code():
    code = []
    for _ in range(4):
        code.append(random.randint(1, 6))
    return code

def get_user_guess():
    while True:
        try:
            guess = input("Enter your guess (4 digits between 1 and 6, e.g., 1234): ")
            if len(guess) != 4:
                raise ValueError("Guess must be 4 digits long.")
            guess = [int(digit) for digit in guess]
            if not all(1 <= digit <= 6 for digit in guess):
                raise ValueError("Each digit in the guess must be between 1 and 6.")
            return guess
        except ValueError as e:
            print(f"Invalid input: {e}")

def check_guess(secret_code, user_guess):
    correct_digits = sum(1 for i, digit in enumerate(user_guess) if digit == secret_code[i])
    incorrect_digits = sum(1 for digit in user_guess if digit in secret_code)
    incorrect_digits -= correct_digits
    return correct_digits, incorrect_digits

def main():
    print("Welcome to Mastermind!")
    secret_code = generate_secret_code()
    attempts = 0

    while True:
        attempts += 1
        user_guess = get_user_guess()
        correct, incorrect = check_guess(secret_code, user_guess)

        print(f"Correct digits: {correct}")
        print(f"Incorrect digits in the wrong position: {incorrect}")

        if correct == 4:
            print(f"Congratulations! You guessed the secret code {secret_code} in {attempts} attempts!")
            break

if __name__ == "__main__":
    main()
