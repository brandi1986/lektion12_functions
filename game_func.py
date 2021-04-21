def play_game():
    import random
    import json
    import datetime

    secret = random.randint(1, 30)
    attempts = 0
    name = input("Wie ist dein Name?")
    wrong_guesses = []
    score_list_dict = get_score_list()


    while True:
        guess = int(input("Rate die geheime Nummer (zwischen 1 und 30): "))
        attempts += 1

        if guess == secret:
            print("Du hast sie erraten. Es war die Nummer " + str(secret))
 /           print("Versuche gebraucht " + str(attempts))

            dict_entry = {
                "name": name,
                "attempts": attempts,
                "date": str(datetime.datetime.now()),
                "secret": secret,
                "wrong_guesses": wrong_guesses,
            }
            score_list_dict.append(dict_entry)
            with open("score_dict.json", "w") as file_handle:
                file_handle.write(json.dumps(score_list_dict))
            break

        elif guess > secret:
            print("Dein Versuch war Falsch, probiere eine kleinere Zahl")
        elif guess < secret:
            print("Dein Versuch war Falsch, probiere eine größere Zahl")
        wrong_guesses.append(guess)


def get_score_list():
    import json

    with open("score_dict.json", "r") as score_file:
        score_list_dict = json.loads(score_file.read())
        return score_list_dict

def get_top_scores():
    import operator
    score_list_dict = get_score_list()
    top_score_list = sorted(score_list_dict, key=operator.itemgetter('attempts'))[:3]
    return top_score_list


