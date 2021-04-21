from game_func import *

while True:
    selection = input("Möchtest du 1) ein neues Spiel starten, 2) die Bestenliste sehen, oder 3) das Spiel beenden?")

    if selection == "1":
        play_game()
    elif selection == "2":
        for score_dict in get_top_scores():
            score_top = "Spieler {0} hat {1} Versuche gebraucht {2}. Die Geheime Nummer war {3}. Die falschen Versuche waren {4}"\
                        .format(score_dict.get("name"),
                        str(score_dict.get("attempts")),6
                        score_dict.get("date"),
                        score_dict.get("secret"),
                        score_dict.get("wrong_guesses"))
            print(score_top)
    else:
        break
