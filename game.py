import random

USER_PROMPT = "guess a number between {} and {}: \n"
LOWEST_NUMBER = 1
HIGHEST_NUMBER = 10

while True:

    randomNumber = random.randint(LOWEST_NUMBER, HIGHEST_NUMBER)
    userGuess = 0

    while randomNumber != userGuess:

        userPrompt = USER_PROMPT.format(LOWEST_NUMBER, HIGHEST_NUMBER)
        userGuess = input(userPrompt)
        userGuess = int(userGuess)

        print("you guessed:", userGuess)

        if randomNumber > userGuess:
            print("the number is higher!")

        elif randomNumber < userGuess:
            print("the number is lower!")


    print("you are correct! yay!")
    print("")

    playAgain = input("Do you want to play again? y/n ")

    if playAgain == "n":
        break