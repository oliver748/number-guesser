import secrets
import os


def generate_number():
    secrets_class = secrets.SystemRandom()
    return secrets_class.randint(1, 10)


def check_number(input, game_number):
    if input == game_number:
        return True
    elif input > game_number:
        return "lower"
    elif input < game_number:
        return "higher"


def get_user_input(category, game_number):
    user_input = input("-> ")
    if category:
        if user_input == "s":
            return True
    else:
        int_user_input = int(user_input)
        return check_number(int_user_input, game_number)


def app():
    clear()
    guess_num = 0
    print(
        'Welcome!\n\nThis game is about guessing the correct number using the fewest guesses possible!\n\nInstructions:\nTo start the game, type: "s"\nTo quit the game, type: "q"\n'
    )

    if get_user_input(1, 0):
        clear()
        game_number = generate_number()
        while True:
            guess_num += 1
            print("Guess a number between 1 and 10")
            input_response = get_user_input(0, game_number)
            clear()
            if input_response == True:
                print(
                    f"You used {guess_num} guess(es) to find {game_number} which is the correct number!"
                )
                break
            else:
                print(f"Try to guess a {input_response} number!")


if __name__ == "__main__":
    clear = lambda: os.system("cls")
    app()
