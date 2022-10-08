import random


def choose_level():
    print("How hard do you want the game to be?")
    print("1 - Easy - 25 chances to try")
    print("2 - Medium - 15 chances to try")
    print("3 - Hard - 5 chances to try")

    while True:
        try:
            level = int(input("Choose the difficulty level (1 or 2 or 3): "))
            if(level < 1 or level > 3):
                print("Not a valid level.")
                continue
            break
        except ValueError:
            print("Invalid choice.")

    if level == 1:
        chances = 25
    elif level == 2:
        chances = 15
    else:
        chances = 5

    return chances


def calculate_score(points, number, guess):
    lost_points = abs(number - guess)
    points = points - lost_points

    return points


def save_highest_score(score):
    record = 0

    try:
        with open("score.txt", "r") as score_file:
            record_line = score_file.read()
            if record_line:
                record = int(record_line)
                print(f"The record for this game is: {record} points.")
    except FileNotFoundError:
        print("There was no champion")

    if score > record:
        print("You are the new champion!")
        with open("score.txt", "w") as score_file:
            score_file.write(str(score))
    else:
        print("Try again to beat the champion!")


def play_game(chances):
    number = random.randint(1, 100)
    points = 9999

    for turn in range(1, chances + 1):
        print(f"-> Chance {turn} out of {chances}")

        while True:
            try:
                guess = int(input("Type a number between 1 and 100: "))
                if(guess < 1 or guess > 100):
                    print("Your guess must be between 1 and 100!")
                    continue
                break
            except ValueError:
                print("Invalid guess.")

        if guess == number:
            print(f">> You nailed it! Final score: {points} <<")
            save_highest_score(points)
            break
        else:
            if guess > number:
                print("Your guess was too high, try a lower number.")
            elif guess < number:
                print("Your guess was too low, try a higher number.")

            points = calculate_score(points, number, guess)

        if turn == chances:
            print(">> You ran out of chances! <<")
            print(f"The right number is: {number}")

    print("Game Over!")


if __name__ == "__main__":
    print("###############################")
    print("Welcome to the Guessing game!")
    print("Guess the number from 1 to 100")
    print("###############################")

    chances = choose_level()

    play_game(chances)
