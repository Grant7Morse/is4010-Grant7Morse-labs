import random

def generate_mad_lib(adjective, noun, verb):
    """
    Generates a short story using the provided words.

    Parameters
    ----------
    adjective : str
        An adjective to use in the story.
    noun : str
        A noun to use in the story.
    verb : str
        A past-tense verb to use in the story.

    Returns
    -------
    str
        A formatted story string that incorporates all three input words.
    """
    return (
        f"Yesterday, a {adjective} {noun} suddenly {verb} down the street, "
        f"and everyone laughed because it looked unreal."
    )


def guessing_game():
    """
    Plays a number guessing game with the user.
    """
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    guess = None
    while guess != secret_number:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess > secret_number:
            print("Too high! Try again.")
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")


if __name__ == '__main__':
    guessing_game()
