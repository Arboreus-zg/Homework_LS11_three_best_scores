import datetime
import random
import json

player = input("Please enter your name: ")
player = player.lower()

secret = random.randint(1, 30)
attempts = 0

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())

#ovdje sam zapeo na listi najbolja tri rezultata, zasad dobijem poruku Non
    best_score_list = score_list.sort(key=lambda k: k['attempts'], reverse=True)
    print("Best three scores: " + str(best_score_list)[:3])

for score_dict in score_list:
    score_text = "Player {0} had {1} attempts on {2}. The secret number was {3}. The wrong guesses were: {4}".format(score_dict.get("player_name"),
                                                                                         str(score_dict.get(
                                                                                             "attempts")),
                                                                                         score_dict.get("date"),
                                                                                         score_dict.get(
                                                                                             "secret_number"),
                                                                                         score_dict.get("wrong_guesses"))
    print(score_text)

wrong_guesses = []

while True:
    guess = int(input("Guess the secret number between 1 and 30: "))
    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "player_name": player,
                           "secret_number": secret, "wrong_guesses": wrong_guesses})

        with open("score_list.txt", "w") as score_file: \
                score_file.write(json.dumps(score_list))

        print("You have guessed it - congratulations! It's number: " + str(secret))
        print("Attempts needed: " + str(attempts))
        break

    elif guess > secret:
        print("Your guess is not correct. Try something smaller.")

    elif guess < secret:
        print("Your guess is not correct. Try something bigger.")

    wrong_guesses.append(guess)