import random

def main():
    wins = 0
    ties = 0
    losses = 0

    # Create a loop that continues as long as the user wants to play.
    while True:

        # Randomly choose the computer between 'R', 'P', or 'S'
        computer_choice = random.choice(['R', 'P', 'S'])

        # Prompt the user for their RPS selection
        user_choice = input("Enter your choice (R for rock, P for paper, S for scissors): ").upper()
        if user_choice not in ['R', 'P', 'S']:
            print("Invalid input. Please enter 'R', 'P', or 'S'.")
            continue

        # Determine winner and state what happened to the user
        if user_choice == computer_choice:
            print(f"Tie game! You both chose {user_choice}.")
            ties += 1
        elif (user_choice == 'R' and computer_choice == 'S') or (user_choice == 'P' and computer_choice == 'R') or (user_choice == 'S' and computer_choice == 'P'):
            print(f"You win! :) {user_choice} beats {computer_choice}.")
            wins += 1
        else:
            print(f"You lost... :( {computer_choice} beats {user_choice}.")
            losses += 1 

        # Ask the user if they would like to play again.
        play_again = input("Rematch? (Y/N): ").upper()
        if play_again != 'Y':
            break

    # In the end, print the stats
    print("Wins \t Ties \t Losses")
    print("---- \t ---- \t ------")
    print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
    main()
