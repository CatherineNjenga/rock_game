import random


def run_game():
    # Options available to the player.
    player_options = {
    "r": "Rock",
    "p": "Paper",
    "s": "Scissors"
    }

    # Prompt to the user/directions on how to play the game.
    prompt = "\nPlease pick an option(r/p/s):"
    prompt += "\nr for Rock, p for Paper and s for Scissors: "

    # An active flag to start the while loop
    active = True
    while active: 
        player_choice = input(prompt)
        auto_choice =  random.choice(list(player_options))
        if player_choice == "r" or player_choice == "p" or player_choice == "s":
            break
        else:
            print("\nInvalid option.")
            continue

    print(f"Player({player_options[player_choice]}) : CPU({player_options[auto_choice]})")

    if player_options[player_choice] == "Rock" and player_options[auto_choice] == "Scissors":
        print("Player wins!")
    elif player_options[player_choice] == "Paper" and player_options[auto_choice] == "Rock":
        print("Player wins!")
    elif player_options[player_choice] == "Scissors" and player_options[auto_choice] == "Paper":
        print("Player wins!")
    elif player_options[auto_choice] == "Rock" and player_options[player_choice] == "Scissors":
        print("CPU wins!")
    elif player_options[auto_choice] == "Paper" and player_options[player_choice] == "Rock":
        print("CPU wins!")
    elif player_options[auto_choice] == "Scissors" and player_options[player_choice] == "Paper":
        print("CPU wins!")
    else:
        print("It is a tie!")
        # Incase of a tie, re-run the game.
        run_game()
run_game()
